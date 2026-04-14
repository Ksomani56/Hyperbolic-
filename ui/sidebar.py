import pygame
import config

class Button:
    def __init__(self, rect, text, action_val, is_toggle=False):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action_val = action_val
        self.is_toggle = is_toggle
        self.active = False
        
    def draw(self, surface, font, mouse_pos):
        color = config.COLORS["button_active"] if self.active else \
                config.COLORS["button_hover"] if self.rect.collidepoint(mouse_pos) else \
                config.COLORS["button_bg"]
                
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        
        text_color = config.COLORS["text_highlight"] if self.active else config.COLORS["text"]
        if self.rect.collidepoint(mouse_pos) and not self.active:
            text_color = config.COLORS["text_highlight"]  # brighten text on hover
            
        text_surf = font.render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

class Sidebar:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 14)
        self.header_font = pygame.font.SysFont("Arial", 12, bold=True)
        self.title_font = pygame.font.SysFont("Arial", 18, bold=True)
        self.buttons = []
        self.headers = []
        
        w = config.SIDEBAR_WIDTH - 40
        y = 50
        
        # Tools
        self.headers.append(("TOOLS", y))
        y += 20
        self.buttons.append(Button((20, y, w, 35), "Point Tool", "point", True))
        self.buttons.append(Button((20, y+45, w, 35), "Line Tool", "line", True))
        
        # Advanced Tools
        y += 95
        self.headers.append(("ADVANCED TOOLS", y))
        y += 20
        self.buttons.append(Button((20, y, w, 35), "Triangle Tool", "triangle", True))
        self.buttons.append(Button((20, y+45, w, 35), "Distance Tool", "distance", True))
        self.buttons.append(Button((20, y+90, w, 35), "Parallel Tool", "parallel", True))
        
        # Actions
        y += 140
        self.headers.append(("ACTIONS", y))
        y += 20
        bw = (w - 10) // 2
        self.buttons.append(Button((20, y, bw, 35), "Clear", "clear"))
        self.buttons.append(Button((20 + bw + 10, y, bw, 35), "Undo", "undo"))
        self.buttons.append(Button((20, y+45, w, 35), "Play Actions", "play"))
        
        # Presets
        y += 95
        self.headers.append(("PRESETS", y))
        y += 20
        self.buttons.append(Button((20, y, w, 35), "Load Triangle Demo", "preset_tri"))
        self.buttons.append(Button((20, y+45, w, 35), "Load Parallels Demo", "preset_par"))
        
        # Settings
        y += 95
        self.headers.append(("SETTINGS", y))
        y += 20
        self.buttons.append(Button((20, y, w, 35), "Explain Mode", "explain", True))
        self.buttons.append(Button((20, y+45, w, 35), "Snap to Grid", "snap", True))
        
        # Extras
        y += 95
        self.headers.append(("EXTRAS", y))
        y += 20
        self.buttons.append(Button((20, y, w, 35), "📚 References", "references"))
        
        # Default active tool
        for b in self.buttons:
            if b.action_val == "point":
                b.active = True

    def draw(self, surface, mouse_pos, engine=None):
        if engine:
            self.sync_state(engine.tool, engine.explain_mode, engine.playback.is_playing, engine.playback.is_paused, engine.snap_mode)
            
        pygame.draw.rect(surface, config.COLORS["sidebar_bg"], config.SIDEBAR_RECT)
        pygame.draw.line(surface, config.COLORS["border"], 
                         (config.SIDEBAR_WIDTH, 0), 
                         (config.SIDEBAR_WIDTH, config.WINDOW_HEIGHT), 2)
                         
        header = self.title_font.render("Dual Geometry", True, config.COLORS["text_highlight"])
        surface.blit(header, (20, 15))
        
        for text, y in self.headers:
            header_surf = self.header_font.render(text, True, config.COLORS["border"])
            surface.blit(header_surf, (20, y))
        
        for btn in self.buttons:
            btn.draw(surface, self.font, mouse_pos)
            
    def handle_click(self, pos, current_tool, explain_mode):
        for btn in self.buttons:
            if btn.rect.collidepoint(pos):
                if btn.is_toggle:
                    if btn.action_val in ["point", "line", "triangle", "distance", "parallel"]:
                        # Tool group mutually exclusive
                        for b in self.buttons:
                            if b.action_val in ["point", "line", "triangle", "distance", "parallel"]:
                                b.active = False
                        btn.active = True
                        return 'tool', btn.action_val
                    elif btn.action_val == "explain":
                        btn.active = not btn.active
                        return 'explain', btn.active
                    elif btn.action_val == "snap":
                        btn.active = not btn.active
                        return 'snap', btn.active
                else:
                    return 'action', btn.action_val
        return None, None
        
    def sync_state(self, current_tool, explain_mode, is_playing, is_paused, snap_mode):
        for b in self.buttons:
            if b.action_val in ["point", "line", "triangle", "distance", "parallel"]:
                b.active = (b.action_val == current_tool)
            elif b.action_val == "explain":
                b.active = explain_mode
            elif b.action_val == "snap":
                b.active = snap_mode
            elif b.action_val == "play":
                if not is_playing:
                    b.text = "Play Actions"
                    b.active = False
                elif is_paused:
                    b.text = "Resume Anim"
                    b.active = True
                else:
                    b.text = "Pause Anim"
                    b.active = True
