import config
from utils.math_utils import distance, point_line_distance
from core.objects import Point, Line, Triangle
from core.playback import PlaybackSystem

class Engine:
    def __init__(self):
        self.points = {}
        self.lines = {}
        self.triangles = {}
        self.demos = [] # Used for special standalone geometric demos like parallel postulate
        self._history = []
        
        self.tool = 'point' # 'point', 'line', 'triangle', 'distance', 'parallel'
        
        self.explain_mode = False
        self.snap_mode = False
        self.show_references = False
        self.active_reference = 0
        self.hovered_object = None
        self.selected_object = None
        
        # Tools state
        self.temp_points = [] # Used for multi-point tools
        self.playback = PlaybackSystem()

    def _save_state(self):
        import copy
        self._history.append({
            'points': copy.deepcopy(self.points),
            'lines': copy.deepcopy(self.lines),
            'triangles': copy.deepcopy(self.triangles),
            'demos': copy.deepcopy(self.demos)
        })
        
    def add_point(self, nx, ny):
        if self.snap_mode:
            nx = round(nx / config.GRID_STEP) * config.GRID_STEP
            ny = round(ny / config.GRID_STEP) * config.GRID_STEP
            
        # Clip to near unit disk for sanity (always keeping points inside logical bounds)
        mag = nx*nx + ny*ny
        if mag > 0.98 * 0.98:
            import math
            scale = 0.98 / math.sqrt(mag)
            nx *= scale
            ny *= scale

        p = Point(nx, ny)
        self.points[p.id] = p
        self.playback.add_action("add_point", x=nx, y=ny, id=p.id)
        return p
        
    def add_line(self, p1_id, p2_id):
        if p1_id not in self.points or p2_id not in self.points:
            return None
        l = Line(p1_id, p2_id)
        self.lines[l.id] = l
        self.playback.add_action("add_line", p1=p1_id, p2=p2_id, id=l.id)
        return l
        
    def add_triangle(self, p1_id, p2_id, p3_id):
        t = Triangle(p1_id, p2_id, p3_id)
        self.triangles[t.id] = t
        self.playback.add_action("add_triangle", p1=p1_id, p2=p2_id, p3=p3_id, id=t.id)
        return t
        
    def add_parallel_demo(self, p1_id, p2_id, p3_id):
        import uuid
        demo_id = str(uuid.uuid4())
        demo = {
            "type": "parallel",
            "p1": p1_id,
            "p2": p2_id,
            "p3": p3_id,
            "id": demo_id
        }
        self.demos.append(demo)
        # Snap the base line so users can see the line they are contrasting against.
        # But we do not want to duplicate lines if they used pre-existing ones?
        # A parallel demo visually includes the line anyway. We just keep the demo state.
        self.playback.add_action("add_parallel_demo", p1=p1_id, p2=p2_id, p3=p3_id, id=demo_id)
        return demo_id
        
    def undo(self):
        if self._history:
            state = self._history.pop()
            self.points = state['points']
            self.lines = state['lines']
            self.triangles = state['triangles']
            self.demos = state['demos']
            self.selected_object = None
            self.hovered_object = None
            self.temp_points.clear()
        
    def clear(self):
        self.points.clear()
        self.lines.clear()
        self.triangles.clear()
        self.demos.clear()
        self.temp_points.clear()
        self.selected_object = None
        self.playback.add_action("clear")
        
    def handle_mouse_move(self, nx, ny):
        if self.playback.is_playing:
            return
            
        closest_dist = 0.05
        hovered = None
        
        for p in self.points.values():
            d = distance(nx, ny, p.x, p.y)
            if d < closest_dist:
                closest_dist = d
                hovered = p.id
                
        if not hovered:
            for l in self.lines.values():
                p1 = self.points.get(l.p1_id)
                p2 = self.points.get(l.p2_id)
                if p1 and p2:
                    d = point_line_distance(nx, ny, p1.x, p1.y, p2.x, p2.y)
                    if d < closest_dist:
                        closest_dist = d
                        hovered = l.id
                        
        if not hovered:
            for t in self.triangles.values():
                p1 = self.points.get(t.p1_id)
                p2 = self.points.get(t.p2_id)
                p3 = self.points.get(t.p3_id)
                if p1 and p2 and p3:
                    d1 = point_line_distance(nx, ny, p1.x, p1.y, p2.x, p2.y)
                    d2 = point_line_distance(nx, ny, p2.x, p2.y, p3.x, p3.y)
                    d3 = point_line_distance(nx, ny, p3.x, p3.y, p1.x, p1.y)
                    if min(d1, d2, d3) < closest_dist:
                        hovered = t.id
                        
        self.hovered_object = hovered
        
    def handle_tool_click(self, nx, ny):
        if self.playback.is_playing:
            return
            
        if self.hovered_object and self.tool == 'point':
            self.selected_object = self.hovered_object
            return
            
        self.selected_object = None
            
        if self.tool == 'point':
            self._save_state()
            self.add_point(nx, ny)
            
        elif self.tool == 'line':
            if len(self.temp_points) == 0: self._save_state()
            p = self.add_point(nx, ny)
            if p:
                self.temp_points.append(p.id)
                if len(self.temp_points) == 2:
                    self.add_line(self.temp_points[0], self.temp_points[1])
                    self.temp_points = []
                    
        elif self.tool == 'triangle':
            if len(self.temp_points) == 0: self._save_state()
            p = self.add_point(nx, ny)
            if p:
                self.temp_points.append(p.id)
                if len(self.temp_points) == 3:
                    self.add_triangle(self.temp_points[0], self.temp_points[1], self.temp_points[2])
                    self.temp_points = []
                    
        elif self.tool == 'parallel':
            if len(self.temp_points) == 0: self._save_state()
            p = self.add_point(nx, ny)
            if p:
                self.temp_points.append(p.id)
                if len(self.temp_points) == 3:
                    self.add_parallel_demo(self.temp_points[0], self.temp_points[1], self.temp_points[2])
                    self.temp_points = []
                    
        elif self.tool == 'distance':
            if len(self.temp_points) == 0: self._save_state()
            p = self.add_point(nx, ny)
            if p:
                self.temp_points.append(p.id)
                if len(self.temp_points) == 2:
                    l = self.add_line(self.temp_points[0], self.temp_points[1])
                    if l:
                        self.selected_object = l.id
                    self.temp_points = [] 

    def load_preset_triangle(self):
        self.clear()
        p1 = self.add_point(0, 0.5)
        p2 = self.add_point(-0.4, -0.4)
        p3 = self.add_point(0.4, -0.4)
        if p1 and p2 and p3:
            self.add_triangle(p1.id, p2.id, p3.id)

    def load_preset_parallels(self):
        self.clear()
        p1 = self.add_point(-0.8, -0.2)
        p2 = self.add_point(0.8, -0.2)
        if p1 and p2:
            self.add_line(p1.id, p2.id)
            
        p3 = self.add_point(0, 0.3)
        p4 = self.add_point(-0.7, 0.8)
        p5 = self.add_point(0.7, 0.8)
        
        if p3 and p4 and p5:
            self.add_line(p3.id, p4.id)
            self.add_line(p3.id, p5.id)

    def update(self, current_time):
        if self.playback.is_playing and not self.playback.is_paused:
            if self.playback.animating_action is None:
                self._play_next_step()
            else:
                self._advance_animation()

    def _advance_animation(self):
        anim = self.playback.animating_action
        if anim['progress'] >= 1.0:
            # Finalize based on action type
            atype = anim["type"]
            if atype == "add_line":
                l = Line(anim["p1"], anim["p2"])
                l.id = anim["id"]
                self.lines[l.id] = l
            elif atype == "add_triangle_edge":
                l = Line(anim["p1"], anim["p2"])
                l.id = anim["id"]
                # In actual playback, we won't necessarily keep random lines if we replace them with triangles,
                # but to avoid deleting them instantly, we keep them. By PRD, triangles draw borders.
                # Since Triangle object just refers to corners, we can just clear temp lines at the end.
                self.lines[l.id] = l
                
                # Check if it was the last edge of the triangle
                if anim.get("is_last_edge"):
                    t = Triangle(anim["t_p1"], anim["t_p2"], anim["t_p3"])
                    t.id = anim["t_id"]
                    self.triangles[t.id] = t
                    
                    # Remove the 3 temporary lines to clean up engine state
                    for e_id in [anim.get("id"), anim.get("e1_id"), anim.get("e2_id")]:
                        if e_id in self.lines:
                            del self.lines[e_id]
                    
            self.playback.animating_action = None
            self.playback.play_index += 1
        else:
            # Advance progress
            # Applying easing function: 1 - (1 - t)**2
            anim['t'] += self.playback.anim_speed
            # Ensure t doesn't exceed 1.0
            anim['t'] = min(1.0, anim['t'])
            anim['progress'] = 1 - (1 - anim['t'])**2

    def _play_next_step(self):
        if self.playback.play_index == 0:
            self._pre_play_points = self.points.copy()
            self._pre_play_lines = self.lines.copy()
            self._pre_play_triangles = self.triangles.copy()
            self._pre_play_demos = self.demos.copy()
            self.points.clear()
            self.lines.clear()
            self.triangles.clear()
            self.demos.clear()
            
        if self.playback.play_index < len(self.playback.actions):
            action = self.playback.actions[self.playback.play_index]
            atype = action["type"]
            
            if atype == "add_point":
                p = Point(action["x"], action["y"])
                p.id = action["id"]
                self.points[p.id] = p
                self.playback.play_index += 1
            elif atype == "add_line":
                self.playback.animating_action = {
                    "type": "add_line",
                    "p1": action["p1"],
                    "p2": action["p2"],
                    "id": action["id"],
                    "t": 0.0,
                    "progress": 0.0
                }
            elif atype == "add_triangle":
                import uuid
                e1_id = str(uuid.uuid4())
                e2_id = str(uuid.uuid4())
                e3_id = str(uuid.uuid4())
                
                p1, p2, p3 = action["p1"], action["p2"], action["p3"]
                t_id = action.get("id")
                
                action["type"] = "add_triangle_edge"
                action["p1"] = p1
                action["p2"] = p2
                action["id"] = e1_id
                
                self.playback.actions.insert(self.playback.play_index + 1, {
                    "type": "add_triangle_edge",
                    "p1": p2,
                    "p2": p3,
                    "id": e2_id
                })
                self.playback.actions.insert(self.playback.play_index + 2, {
                    "type": "add_triangle_edge",
                    "p1": p3,
                    "p2": p1,
                    "id": e3_id,
                    "is_last_edge": True,
                    "t_id": t_id,
                    "t_p1": p1,
                    "t_p2": p2,
                    "t_p3": p3,
                    "e1_id": e1_id,
                    "e2_id": e2_id
                })
                
                self.playback.animating_action = {
                    "type": "add_triangle_edge",
                    "p1": p1,
                    "p2": p2,
                    "id": e1_id,
                    "t": 0.0,
                    "progress": 0.0
                }
            elif atype == "add_triangle_edge":
                self.playback.animating_action = {
                    "type": "add_triangle_edge",
                    "p1": action["p1"],
                    "p2": action["p2"],
                    "id": action["id"],
                    "t": 0.0,
                    "progress": 0.0,
                    "is_last_edge": action.get("is_last_edge", False),
                    "t_id": action.get("t_id"),
                    "t_p1": action.get("t_p1"),
                    "t_p2": action.get("t_p2"),
                    "t_p3": action.get("t_p3"),
                    "e1_id": action.get("e1_id"),
                    "e2_id": action.get("e2_id")
                }
            elif atype == "add_parallel_demo":
                # We won't animate the parallel demo to keep it crystal clear. Snap instantly.
                demo = {
                    "type": "parallel",
                    "p1": action["p1"],
                    "p2": action["p2"],
                    "p3": action["p3"],
                    "id": action["id"]
                }
                self.demos.append(demo)
                self.playback.play_index += 1
            elif atype == "clear":
                self.points.clear()
                self.lines.clear()
                self.triangles.clear()
                self.demos.clear()
                self.playback.play_index += 1
        else:
            self.playback.is_playing = False
            self.playback.is_paused = False
