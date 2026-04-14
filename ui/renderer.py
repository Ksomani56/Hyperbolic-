import pygame
import math
import config
from utils.math_utils import denormalize_point
from geometry.euclidean import euclidean_distance, euclidean_triangle_angles, get_euclidean_parallel
from geometry.hyperbolic import get_geodesic_arc, hyperbolic_distance, hyperbolic_triangle_angles, get_hyperbolic_parallels

class Renderer:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont("Arial", 14)
        self.big_font = pygame.font.SysFont("Arial", 18, bold=True)
        
    def draw(self, engine):
        self.surface.fill(config.COLORS["background"])
        
        # Draw Backgrounds
        pygame.draw.rect(self.surface, config.COLORS["panel_bg"], config.EUCLIDEAN_RECT)
        pygame.draw.rect(self.surface, config.COLORS["panel_bg"], config.HYPERBOLIC_RECT)
        
        # Grid/axes for Euclidean
        ecx, ecy = config.EUCLIDEAN_RECT[0] + config.EUCLIDEAN_RECT[2]//2, config.EUCLIDEAN_RECT[1] + config.EUCLIDEAN_RECT[3]//2
        if engine.snap_mode:
            # Draw subtle grid lines
            step = (config.EUCLIDEAN_RECT[2] / 2) * config.GRID_STEP
            for i in range(int(2 / config.GRID_STEP)):
                dx = config.EUCLIDEAN_RECT[0] + i * step
                pygame.draw.line(self.surface, (30, 30, 30), (dx, config.EUCLIDEAN_RECT[1]), (dx, config.EUCLIDEAN_RECT[1]+config.EUCLIDEAN_RECT[3]))
            for i in range(int(2 / config.GRID_STEP)):
                dy = config.EUCLIDEAN_RECT[1] + i * step
                if dy <= config.EUCLIDEAN_RECT[1] + config.EUCLIDEAN_RECT[3]:
                    pygame.draw.line(self.surface, (30, 30, 30), (config.EUCLIDEAN_RECT[0], dy), (config.EUCLIDEAN_RECT[0]+config.EUCLIDEAN_RECT[2], dy))
                    
        # Primary Axes
        pygame.draw.line(self.surface, config.COLORS["button_hover"], (config.EUCLIDEAN_RECT[0], ecy), (config.EUCLIDEAN_RECT[0]+config.EUCLIDEAN_RECT[2], ecy))
        pygame.draw.line(self.surface, config.COLORS["button_hover"], (ecx, config.EUCLIDEAN_RECT[1]), (ecx, config.EUCLIDEAN_RECT[1]+config.EUCLIDEAN_RECT[3]))
        
        # Disk for Hyperbolic
        hcx, hcy = config.HYPERBOLIC_RECT[0] + config.HYPERBOLIC_RECT[2]//2, config.HYPERBOLIC_RECT[1] + config.HYPERBOLIC_RECT[3]//2
        rad_h = (min(config.HYPERBOLIC_RECT[2], config.HYPERBOLIC_RECT[3]) // 2) * config.DISK_RADIUS_RATIO
        pygame.draw.circle(self.surface, config.COLORS["disk_bg"], (hcx, hcy), int(rad_h))
        
        if engine.snap_mode:
            # Draw hyperbolic grid (Module 11)
            for i in range(1, 10):
                r_h = i * 0.5
                r_e = math.tanh(r_h / 2)
                pygame.draw.circle(self.surface, (50, 50, 50), (hcx, hcy), int(r_e * rad_h), 1)
            
            num_spokes = 12
            for i in range(num_spokes):
                theta = i * math.pi / num_spokes
                dx = math.cos(theta) * rad_h
                dy = math.sin(theta) * rad_h
                pygame.draw.line(self.surface, (50, 50, 50), (hcx - dx, hcy - dy), (hcx + dx, hcy + dy), 1)
        
        pygame.draw.circle(self.surface, config.COLORS["border"], (hcx, hcy), int(rad_h), 2)
        
        # Draw geometries
        self._draw_euclidean(engine)
        self._draw_hyperbolic(engine)
        
        # Draw live measurement overlay for selected objects
        if engine.selected_object:
            self._draw_measurement_overlay(engine)
        
        # Draw titles
        e_title = self.big_font.render("Euclidean Space", True, config.COLORS["text_highlight"])
        self.surface.blit(e_title, (config.EUCLIDEAN_RECT[0] + 10, 10))
        
        h_title = self.big_font.render("Hyperbolic Space (Poincaré Disk)", True, config.COLORS["text_highlight"])
        self.surface.blit(h_title, (config.HYPERBOLIC_RECT[0] + 10, 10))
        
        if engine.explain_mode:
            self._draw_explain_tooltips(engine)
            
        # Draw Progress Indicator toolbar
        if getattr(engine.playback, 'is_playing', False):
            total = len(engine.playback.actions)
            if total > 0:
                current = engine.playback.play_index
                base_prog = current / total
                fraction = 0
                if engine.playback.animating_action:
                    fraction = (engine.playback.animating_action.get('progress', 0) * (1 / total))
                
                bar_width = int((base_prog + fraction) * (config.WINDOW_WIDTH - config.SIDEBAR_WIDTH))
                pygame.draw.rect(self.surface, config.COLORS["button_active"], (config.SIDEBAR_WIDTH, config.WINDOW_HEIGHT - 4, bar_width, 4))
            
    def _get_line_color(self, obj_id, engine, base_color):
        if obj_id == engine.hovered_object or obj_id == engine.selected_object:
            return config.COLORS["highlight"]
        return base_color
        
    def _get_thickness(self, obj_id, engine):
        if obj_id == engine.hovered_object or obj_id == engine.selected_object:
            return config.LINE_WIDTH + 2
        return config.LINE_WIDTH

    def _draw_euclidean(self, engine):
        for line in engine.lines.values():
            p1 = engine.points.get(line.p1_id)
            p2 = engine.points.get(line.p2_id)
            if not p1 or not p2: continue
            s1 = denormalize_point(p1.x, p1.y, config.EUCLIDEAN_RECT)
            s2 = denormalize_point(p2.x, p2.y, config.EUCLIDEAN_RECT)
            col = self._get_line_color(line.id, engine, config.COLORS["e_line"])
            thick = self._get_thickness(line.id, engine)
            pygame.draw.line(self.surface, col, s1, s2, thick)
            
        for tri in engine.triangles.values():
            p1 = engine.points.get(tri.p1_id)
            p2 = engine.points.get(tri.p2_id)
            p3 = engine.points.get(tri.p3_id)
            if not p1 or not p2 or not p3: continue
            s1 = denormalize_point(p1.x, p1.y, config.EUCLIDEAN_RECT)
            s2 = denormalize_point(p2.x, p2.y, config.EUCLIDEAN_RECT)
            s3 = denormalize_point(p3.x, p3.y, config.EUCLIDEAN_RECT)
            col = self._get_line_color(tri.id, engine, config.COLORS["e_triangle"])
            thick = self._get_thickness(tri.id, engine)
            pygame.draw.line(self.surface, col, s1, s2, thick)
            pygame.draw.line(self.surface, col, s2, s3, thick)
            pygame.draw.line(self.surface, col, s3, s1, thick)

        for point in engine.points.values():
            s = denormalize_point(point.x, point.y, config.EUCLIDEAN_RECT)
            col = self._get_line_color(point.id, engine, config.COLORS["e_point"])
            rad = config.POINT_RADIUS + (2 if point.id in (engine.hovered_object, engine.selected_object) else 0)
            pygame.draw.circle(self.surface, col, s, rad)
            
        anim = engine.playback.animating_action
        if anim and anim["type"] in ["add_line", "add_triangle_edge"]:
            p1 = engine.points.get(anim["p1"])
            p2 = engine.points.get(anim["p2"])
            if p1 and p2:
                t = anim["progress"]
                s1 = denormalize_point(p1.x, p1.y, config.EUCLIDEAN_RECT)
                s2 = denormalize_point(p2.x, p2.y, config.EUCLIDEAN_RECT)
                cx = s1[0] + t * (s2[0] - s1[0])
                cy = s1[1] + t * (s2[1] - s1[1])
                pygame.draw.line(self.surface, config.COLORS["e_line"], s1, (cx, cy), config.LINE_WIDTH)
                pygame.draw.circle(self.surface, (255, 255, 0), (int(cx), int(cy)), config.POINT_RADIUS + 1)
                
        for demo in engine.demos:
            if demo["type"] == "parallel":
                p1 = engine.points.get(demo["p1"])
                p2 = engine.points.get(demo["p2"])
                p3 = engine.points.get(demo["p3"])
                if p1 and p2 and p3:
                    end1, end2 = get_euclidean_parallel((p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y))
                    s1 = denormalize_point(end1[0], end1[1], config.EUCLIDEAN_RECT)
                    s2 = denormalize_point(end2[0], end2[1], config.EUCLIDEAN_RECT)
                    pygame.draw.line(self.surface, config.COLORS["e_line"], s1, s2, config.LINE_WIDTH)
                    
                    text = self.big_font.render("1 Parallel Line", True, config.COLORS["highlight"])
                    sp3 = denormalize_point(p3.x, p3.y, config.EUCLIDEAN_RECT)
                    self.surface.blit(text, (sp3[0] + 15, sp3[1] - 15))

    def _draw_hyperbolic(self, engine):
        def draw_geodesic(p1, p2, color, thick):
            geo = get_geodesic_arc((p1.x, p1.y), (p2.x, p2.y))
            if geo[0] == 'line':
                s1 = denormalize_point(p1.x, p1.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                s2 = denormalize_point(p2.x, p2.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                pygame.draw.line(self.surface, color, s1, s2, thick)
            elif geo[0] == 'arc':
                _, cx, cy, r, a1, a2 = geo
                scx, scy = denormalize_point(cx, cy, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                scale = (min(config.HYPERBOLIC_RECT[2], config.HYPERBOLIC_RECT[3]) / 2) * config.DISK_RADIUS_RATIO
                sr = r * scale
                
                diff = (a2 - a1) % (2*math.pi)
                if diff > math.pi:
                    diff -= 2*math.pi
                    
                steps = max(15, int(abs(diff) * sr / 4))
                pts = []
                for i in range(steps + 1):
                    t = a1 + diff * (i / steps)
                    lx = cx + r * math.cos(t)
                    ly = cy + r * math.sin(t)
                    m_sq = lx*lx + ly*ly
                    if m_sq <= 1.0001: 
                        sx, sy = denormalize_point(lx, ly, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                        pts.append((sx, sy))
                
                if len(pts) > 1:
                    pygame.draw.lines(self.surface, color, False, pts, thick)
                    
        def draw_full_geodesic(geo, color, thick):
            if geo[0] == 'line':
                den = math.sqrt(geo[2][0]**2 + geo[2][1]**2)
                if den > 0:
                    ux, uy = geo[2][0]/den, geo[2][1]/den
                    s1 = denormalize_point(ux, uy, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                    s2 = denormalize_point(-ux, -uy, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                    pygame.draw.line(self.surface, color, s1, s2, thick)
            elif geo[0] == 'arc':
                _, cx, cy, r, _, _ = geo
                D_sq = cx**2 + cy**2
                if D_sq <= 1: return
                D = math.sqrt(D_sq)
                mx, my = cx / D_sq, cy / D_sq
                h = math.sqrt(1 - 1/D_sq)
                dirx, diry = -cy / D, cx / D
                ix1, iy1 = mx + h * dirx, my + h * diry
                ix2, iy2 = mx - h * dirx, my - h * diry
                a1 = math.atan2(iy1 - cy, ix1 - cx)
                a2 = math.atan2(iy2 - cy, ix2 - cx)
                
                diff = (a2 - a1) % (2*math.pi)
                if diff > math.pi:
                    diff -= 2*math.pi
                    
                scale = (min(config.HYPERBOLIC_RECT[2], config.HYPERBOLIC_RECT[3]) / 2) * config.DISK_RADIUS_RATIO
                sr = r * scale
                steps = max(15, int(abs(diff) * sr / 4))
                pts = []
                for i in range(steps + 1):
                    t = a1 + diff * (i / steps)
                    lx = cx + r * math.cos(t)
                    ly = cy + r * math.sin(t)
                    m_sq = lx*lx + ly*ly
                    if m_sq <= 1.0001: 
                        sx, sy = denormalize_point(lx, ly, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                        pts.append((sx, sy))
                if len(pts) > 1:
                    pygame.draw.lines(self.surface, color, False, pts, thick)
            
        for line in engine.lines.values():
            p1 = engine.points.get(line.p1_id)
            p2 = engine.points.get(line.p2_id)
            if p1 and p2:
                col = self._get_line_color(line.id, engine, config.COLORS["h_line"])
                thick = self._get_thickness(line.id, engine)
                draw_geodesic(p1, p2, col, thick)
            
        for tri in engine.triangles.values():
            p1 = engine.points.get(tri.p1_id)
            p2 = engine.points.get(tri.p2_id)
            p3 = engine.points.get(tri.p3_id)
            if not p1 or not p2 or not p3: continue
            
            col = self._get_line_color(tri.id, engine, config.COLORS["h_triangle"])
            thick = self._get_thickness(tri.id, engine)
            draw_geodesic(p1, p2, col, thick)
            draw_geodesic(p2, p3, col, thick)
            draw_geodesic(p3, p1, col, thick)

        for point in engine.points.values():
            s = denormalize_point(point.x, point.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
            col = self._get_line_color(point.id, engine, config.COLORS["h_point"])
            rad = config.POINT_RADIUS + (2 if point.id in (engine.hovered_object, engine.selected_object) else 0)
            pygame.draw.circle(self.surface, col, s, rad)
            
        anim = engine.playback.animating_action
        if anim and anim["type"] in ["add_line", "add_triangle_edge"]:
            p1 = engine.points.get(anim["p1"])
            p2 = engine.points.get(anim["p2"])
            if p1 and p2:
                d_t = anim["progress"]
                geo = get_geodesic_arc((p1.x, p1.y), (p2.x, p2.y))
                if geo[0] == 'line':
                    s1 = denormalize_point(p1.x, p1.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                    s2 = denormalize_point(p2.x, p2.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                    cx = s1[0] + d_t * (s2[0] - s1[0])
                    cy = s1[1] + d_t * (s2[1] - s1[1])
                    pygame.draw.line(self.surface, config.COLORS["h_line"], s1, (cx, cy), config.LINE_WIDTH)
                    pygame.draw.circle(self.surface, (255, 255, 0), (int(cx), int(cy)), config.POINT_RADIUS + 1)
                elif geo[0] == 'arc':
                    _, cx, cy, r, a1, a2 = geo
                    diff = (a2 - a1) % (2*math.pi)
                    if diff > math.pi:
                        diff -= 2*math.pi
                        
                    a_current = a1 + d_t * diff
                    scx, scy = denormalize_point(cx, cy, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                    scale = (min(config.HYPERBOLIC_RECT[2], config.HYPERBOLIC_RECT[3]) / 2) * config.DISK_RADIUS_RATIO
                    sr = r * scale
                    
                    current_diff = a_current - a1
                    steps = max(5, int(abs(current_diff) * sr / 4))
                    pts = []
                    for i in range(steps + 1):
                        t_an = a1 + current_diff * (i / steps) if steps > 0 else a1
                        lx = cx + r * math.cos(t_an)
                        ly = cy + r * math.sin(t_an)
                        m_sq = lx*lx + ly*ly
                        if m_sq <= 1.0001: 
                            sx, sy = denormalize_point(lx, ly, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                            pts.append((sx, sy))
                    
                    if len(pts) > 1:
                        pygame.draw.lines(self.surface, config.COLORS["h_line"], False, pts, config.LINE_WIDTH)
                    if len(pts) > 0:
                        last_pt = pts[-1]
                        pygame.draw.circle(self.surface, (255, 255, 0), (int(last_pt[0]), int(last_pt[1])), config.POINT_RADIUS + 1)

        for demo in engine.demos:
            if demo["type"] == "parallel":
                p1 = engine.points.get(demo["p1"])
                p2 = engine.points.get(demo["p2"])
                p3 = engine.points.get(demo["p3"])
                if p1 and p2 and p3:
                    parallels = get_hyperbolic_parallels((p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y), 7)
                    for pline in parallels:
                        draw_full_geodesic(pline, config.COLORS["h_line"], config.LINE_WIDTH)
                        
                    text = self.big_font.render("Infinite Parallel Lines", True, config.COLORS["highlight"])
                    sp3 = denormalize_point(p3.x, p3.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                    
                    bg_rect = pygame.Rect(sp3[0]+15, sp3[1]-15, text.get_width()+6, text.get_height()+4)
                    pygame.draw.rect(self.surface, (0,0,0,150), bg_rect, border_radius=3)
                    self.surface.blit(text, (sp3[0] + 18, sp3[1] - 13))

    def _draw_measurement_overlay(self, engine):
        obj_id = engine.selected_object
        if obj_id in engine.lines:
            l = engine.lines[obj_id]
            p1 = engine.points.get(l.p1_id)
            p2 = engine.points.get(l.p2_id)
            if p1 and p2:
                e_d = euclidean_distance((p1.x, p1.y), (p2.x, p2.y))
                h_d = hyperbolic_distance((p1.x, p1.y), (p2.x, p2.y))
                val = "∞" if math.isinf(h_d) else f"{h_d:.2f}"
                
                # Draw on Euclidean
                s1 = denormalize_point(p1.x, p1.y, config.EUCLIDEAN_RECT)
                s2 = denormalize_point(p2.x, p2.y, config.EUCLIDEAN_RECT)
                cx, cy = (s1[0]+s2[0])/2, (s1[1]+s2[1])/2
                text = self.font.render(f"d = {e_d:.2f}", True, config.COLORS["highlight"])
                self.surface.blit(text, (cx+10, cy-10))
                
                # Draw on Hyperbolic
                s1 = denormalize_point(p1.x, p1.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                s2 = denormalize_point(p2.x, p2.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                cx, cy = (s1[0]+s2[0])/2, (s1[1]+s2[1])/2
                text = self.font.render(f"d ≈ {val}", True, config.COLORS["highlight"])
                bg_rect = pygame.Rect(cx+10, cy-10, text.get_width()+6, text.get_height()+4)
                pygame.draw.rect(self.surface, (0,0,0,150), bg_rect, border_radius=3)
                self.surface.blit(text, (cx+13, cy-8))
                
        elif obj_id in engine.triangles:
            t = engine.triangles[obj_id]
            p1 = engine.points.get(t.p1_id)
            p2 = engine.points.get(t.p2_id)
            p3 = engine.points.get(t.p3_id)
            if p1 and p2 and p3:
                ea1, ea2, ea3 = euclidean_triangle_angles((p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y))
                ha1, ha2, ha3 = hyperbolic_triangle_angles((p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y))
                
                ed1 = euclidean_distance((p1.x, p1.y), (p2.x, p2.y))
                ed2 = euclidean_distance((p2.x, p2.y), (p3.x, p3.y))
                ed3 = euclidean_distance((p3.x, p3.y), (p1.x, p1.y))
                s = (ed1 + ed2 + ed3) / 2
                area_e = math.sqrt(max(0, s*(s-ed1)*(s-ed2)*(s-ed3)))
                
                # Euclidean
                s1 = denormalize_point(p1.x, p1.y, config.EUCLIDEAN_RECT)
                s2 = denormalize_point(p2.x, p2.y, config.EUCLIDEAN_RECT)
                s3 = denormalize_point(p3.x, p3.y, config.EUCLIDEAN_RECT)
                cx, cy = (s1[0]+s2[0]+s3[0])/3, (s1[1]+s2[1]+s3[1])/3
                
                e_lines = [
                    f"Sum: {ea1+ea2+ea3:.0f}°",
                    "Defect: 0°",
                    f"Area: {area_e*100:.1f}"
                ]
                
                for i, text_str in enumerate(e_lines):
                    text = self.font.render(text_str, True, config.COLORS["highlight"])
                    self.surface.blit(text, (cx-text.get_width()//2, cy-text.get_height()//2 + i*16 - 16))

                # Hyperbolic
                s1 = denormalize_point(p1.x, p1.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                s2 = denormalize_point(p2.x, p2.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                s3 = denormalize_point(p3.x, p3.y, config.HYPERBOLIC_RECT, config.DISK_RADIUS_RATIO)
                cx, cy = (s1[0]+s2[0]+s3[0])/3, (s1[1]+s2[1]+s3[1])/3
                
                total = ha1+ha2+ha3
                defect = 180.0 - total
                # Area in hyperbolic circle (radius=1) is equal to its defect in radians
                defect_rad = max(0, defect) * (math.pi / 180.0)
                h_lines = [
                    f"Sum: {total:.1f}°",
                    f"Defect: {max(0, defect):.1f}°",
                    f"Area: {defect_rad:.3f}"
                ]
                
                max_w = max(self.font.size(l)[0] for l in h_lines)
                bg_rect = pygame.Rect(cx-max_w//2 - 4, cy - 24, max_w + 8, len(h_lines)*16 + 4)
                pygame.draw.rect(self.surface, (0,0,0,150), bg_rect, border_radius=3)
                
                for i, text_str in enumerate(h_lines):
                    text = self.font.render(text_str, True, config.COLORS["highlight"])
                    self.surface.blit(text, (cx-text.get_width()//2, cy - 20 + i*16))

    def _draw_explain_tooltips(self, engine):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > config.SIDEBAR_WIDTH:
            if engine.hovered_object:
                msg = "Click with Point tool to pin measurements for this geometry."
            else:
                tool_msg = {
                    'point': "Points inside the disk map 1:1, but space expands toward the edge.",
                    'line': "A 'straight line' in hyperbolic space is an arc perpendicular to boundary.",
                    'triangle': "Hyperbolic triangles have angle sums less than 180 degrees.",
                    'distance': "Distances grow exponentially toward the edge of the disk.",
                    'parallel': "Euclidean has 1 parallel line. Hyperbolic has infinite due to negative curvature."
                }
                msg = tool_msg.get(engine.tool, "Hover over objects to see highlights.")
            
            space = "Hyperbolic" if mouse_pos[0] >= config.HYPERBOLIC_RECT[0] else "Euclidean"
            text = self.font.render(f"{space}: {msg}", True, config.COLORS["tooltip_text"])
            
            padding = 10
            rect = pygame.Rect(mouse_pos[0] + 15, mouse_pos[1] + 15, text.get_width() + padding*2, text.get_height() + padding*2)
            
            if rect.right > config.WINDOW_WIDTH:
                rect.right = mouse_pos[0] - 15
                rect.x = rect.right - rect.width
            if rect.bottom > config.WINDOW_HEIGHT:
                rect.bottom = mouse_pos[1] - 15
                rect.y = rect.bottom - rect.height
                
            pygame.draw.rect(self.surface, config.COLORS["tooltip_bg"], rect, border_radius=4)
            pygame.draw.rect(self.surface, config.COLORS["border"], rect, 1, border_radius=4)
            self.surface.blit(text, (rect.x + padding, rect.y + padding))
