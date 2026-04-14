import pygame
import config
from utils.math_utils import normalize_point

class InputHandler:
    def __init__(self, engine, sidebar, ref_modal=None):
        self.engine = engine
        self.sidebar = sidebar
        self.ref_modal = ref_modal
        
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if getattr(self.engine, 'show_references', False) and self.ref_modal:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.ref_modal.handle_click(mouse_pos, self.engine)
                # Block interactions with underlying canvas
                if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
                    continue
                    
            elif event.type == pygame.MOUSEMOTION:
                if mouse_pos[0] > config.SIDEBAR_WIDTH:
                    if config.EUCLIDEAN_RECT[0] <= mouse_pos[0] < config.EUCLIDEAN_RECT[0] + config.EUCLIDEAN_RECT[2]:
                        nx, ny = normalize_point(mouse_pos[0], mouse_pos[1], config.EUCLIDEAN_RECT)
                        self.engine.handle_mouse_move(nx, ny)
                    elif config.HYPERBOLIC_RECT[0] <= mouse_pos[0] < config.HYPERBOLIC_RECT[0] + config.HYPERBOLIC_RECT[2]:
                        nx, ny = normalize_point(mouse_pos[0], mouse_pos[1], config.HYPERBOLIC_RECT, render_scale=config.DISK_RADIUS_RATIO)
                        self.engine.handle_mouse_move(nx, ny)
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    # Check sidebar
                    if mouse_pos[0] < config.SIDEBAR_WIDTH:
                        action_type, val = self.sidebar.handle_click(
                            mouse_pos, self.engine.tool, self.engine.explain_mode
                        )
                        if action_type == 'tool':
                            self.engine.tool = val
                            self.engine.temp_points.clear()
                        elif action_type == 'explain':
                            self.engine.explain_mode = val
                        elif action_type == 'snap':
                            self.engine.snap_mode = val
                        elif action_type == 'action':
                            if val == 'clear':
                                self.engine.clear()
                            elif val == 'play':
                                if not self.engine.playback.is_playing:
                                    self.engine.playback.start_playback()
                                else:
                                    self.engine.playback.toggle_pause()
                            elif val == 'undo':
                                self.engine.undo()
                            elif val == 'preset_tri':
                                self.engine.load_preset_triangle()
                            elif val == 'preset_par':
                                self.engine.load_preset_parallels()
                            elif val == 'references':
                                self.engine.show_references = True
                                from ui.references import auto_select_reference_for_tool
                                auto_select_reference_for_tool(self.engine)
                    else:
                        # Check which panel we are in and normalize coordinates based on it
                        if config.EUCLIDEAN_RECT[0] <= mouse_pos[0] < config.EUCLIDEAN_RECT[0] + config.EUCLIDEAN_RECT[2]:
                            nx, ny = normalize_point(mouse_pos[0], mouse_pos[1], config.EUCLIDEAN_RECT)
                            self.engine.handle_tool_click(nx, ny)
                        elif config.HYPERBOLIC_RECT[0] <= mouse_pos[0] < config.HYPERBOLIC_RECT[0] + config.HYPERBOLIC_RECT[2]:
                            nx, ny = normalize_point(mouse_pos[0], mouse_pos[1], config.HYPERBOLIC_RECT, render_scale=config.DISK_RADIUS_RATIO)
                            self.engine.handle_tool_click(nx, ny)
                            
        self.sidebar.sync_state(self.engine.tool, self.engine.explain_mode, self.engine.playback.is_playing, self.engine.playback.is_paused, self.engine.snap_mode)
        return True
