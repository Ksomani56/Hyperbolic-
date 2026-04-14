import pygame
import config

REFERENCES_DATA = [
    {
        "title": "Parallel Postulate",
        "theory": "The Parallel Postulate (Euclid's Fifth Postulate) fundamentally distinguishes Euclidean geometry from all others. It defines the behavior of lines that never intersect. For over two millennia, mathematicians attempted to prove this postulate using the first four, ultimately realizing that it is independent. Modifying this postulate gives birth to entirely new, logically consistent universes of geometry.",
        "euclidean": "Given a line and a point not on it, exactly one line can be drawn through the point parallel to the given line. The distance between parallel lines remains strictly constant.",
        "hyperbolic": "Given a line and a point not on it, there are infinitely many lines through the point that do not intersect the original line. Parallel lines in hyperbolic space diverge and curve away from each other exponentially.",
        "author": "Euclid, challenged by Nikolai Lobachevsky and János Bolyai",
        "tool_link": "parallel"
    },
    {
        "title": "Triangle Angle Sum",
        "theory": "The sum of the interior angles of a triangle is a direct measure of the curvature of the space it inhabits. In flat (zero curvature) space, triangles are rigid. In curved space, the angles warp to accommodate the geometry. The difference between the Euclidean 180° and the actual angle sum is called the 'Angle Defect'.",
        "euclidean": "The angles of any triangle will always sum to exactly 180°, regardless of how large or small the triangle is.",
        "hyperbolic": "The sum of the angles is strictly less than 180°. As a hyperbolic triangle grows larger, its angles become sharper and sharper, eventually approaching 0°. Therefore, the maximum area of a hyperbolic triangle is strictly finite and bounded by its angle defect!",
        "insight": "Angle defect reflects curvature. Area is directly proportional to this defect: Area = k² * (π - A - B - C).",
        "author": "Carl Friedrich Gauss",
        "tool_link": "triangle"
    },
    {
        "title": "Hyperbolic Geometry Basics",
        "theory": "Also known as Lobachevskian geometry, this is a non-Euclidean geometry characterized by negative constant curvature. While spherical geometry models a globe, hyperbolic geometry models a saddle-shape. Inside our Poincaré disk model, an entire infinite mathematical universe is projected onto a finite Euclidean circle.",
        "insight": "Space expands outwards exponentially. This means that simply 'walking' towards the edge of the disk would take an eternity, as the 'rulers' used to measure distance shrink proportionally near the boundary.",
        "author": "Nikolai Lobachevsky & János Bolyai",
        "tool_link": ""
    },
    {
        "title": "Geodesics (Shortest Path)",
        "theory": "A geodesic represents the straightest and shortest possible path between two points within a given geometry. While light travels in straight lines in flat space, in curved space, the very fabric of space is warped, forcing the shortest path to physically bend across the coordinate plane.",
        "euclidean": "Geodesics are perfectly straight linear segments.",
        "hyperbolic": "Geodesics appear as curved arcs. Specifically, in the Poincaré disk model, they are represented by segments of Euclidean circles that intersect the outer boundary of the disk at perfect 90-degree right angles.",
        "author": "Bernhard Riemann",
        "tool_link": "line"
    },
    {
        "title": "Distance and Infinity",
        "theory": "The metric formula governing distance defines how we measure the separation between two points. In hyperbolic space, Euclidean coordinates deceive the eye, as the standard Pythagorean theorem breaks down completely.",
        "insight": "The boundary of the Poincaré disk is mathematically infinitely far away. As an object moves towards the edge, it requires exponentially more energy to cover the same visual distance, causing objects to appear to shrink infinitely to external Euclidean observers.",
        "author": "Henri Poincaré",
        "tool_link": "distance"
    },
    {
        "title": "Circle Radial Growth",
        "theory": "In classical geometry, measuring the circumference of a circle given its radius is dictated by the constant Pi. However, in non-Euclidean spaces, the ratio between radius and area undergoes massive distortion based on the scale of the object.",
        "insight": "While a Euclidean circle's circumference grows linearly (C = 2πr), a Hyperbolic circle's area and circumference grow exponentially. A small circle behaves nearly Euclidean, but a massive circle contains vastly more internal space than its radius would traditionally suggest.",
        "author": "",
        "tool_link": ""
    },
    {
        "title": "Hyperbolic Tessellation",
        "theory": "Tessellation refers to tiling a surface with repeating geometric shapes without any gaps or overlaps. Because hyperbolic polygons have mathematically smaller interior angles than standard polygons, shapes that could never tile flat space (like regular octagons or heptagons) can effortlessly tile the hyperbolic plane together.",
        "author": "Maurits Cornelis Escher (Artist)",
        "tool_link": ""
    }
]

class ReferencesModal:
    def __init__(self):
        self.rect = pygame.Rect(config.WINDOW_WIDTH // 2 - 400, config.WINDOW_HEIGHT // 2 - 250, 800, 500)
        self.close_rect = pygame.Rect(self.rect.right - 40, self.rect.top + 10, 30, 30)
        
        self.nav_width = 250
        self.content_rect = pygame.Rect(self.rect.left + self.nav_width, self.rect.top, self.rect.width - self.nav_width, self.rect.height)
        
        self.font_title = pygame.font.SysFont("Arial", 28, bold=True)
        self.font_header = pygame.font.SysFont("Arial", 18, bold=True)
        self.font_body = pygame.font.SysFont("Arial", 16)
        self.font_nav = pygame.font.SysFont("Arial", 15)
        
    def draw_text_wrapped(self, surface, text, font, color, rect):
        words = text.split(' ')
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            fw, fh = font.size(' '.join(current_line))
            if fw > rect.width:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
            
        y = rect.y
        for line in lines:
            text_surf = font.render(line, True, color)
            surface.blit(text_surf, (rect.x, y))
            y += font.get_linesize()
        return y - rect.y

    def draw(self, surface, engine, mouse_pos):
        # Dim background
        dim_surf = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.SRCALPHA)
        dim_surf.fill((0, 0, 0, 150))
        surface.blit(dim_surf, (0, 0))
        
        # Draw main modal background
        pygame.draw.rect(surface, config.COLORS["panel_bg"], self.rect, border_radius=8)
        pygame.draw.rect(surface, config.COLORS["border"], self.rect, 2, border_radius=8)
        
        # Draw navigation pane (Left)
        nav_rect = pygame.Rect(self.rect.left, self.rect.top, self.nav_width, self.rect.height)
        pygame.draw.rect(surface, config.COLORS["sidebar_bg"], nav_rect, border_bottom_left_radius=8, border_top_left_radius=8)
        pygame.draw.line(surface, config.COLORS["border"], (nav_rect.right, nav_rect.top), (nav_rect.right, nav_rect.bottom), 2)
        
        nav_top_text = self.font_header.render("📚 Browse Topics", True, config.COLORS["text_highlight"])
        surface.blit(nav_top_text, (nav_rect.x + 15, nav_rect.y + 20))
        
        y_offset = nav_rect.y + 60
        for i, ref in enumerate(REFERENCES_DATA):
            btn_rect = pygame.Rect(nav_rect.x + 10, y_offset, nav_rect.width - 20, 35)
            
            is_hover = btn_rect.collidepoint(mouse_pos)
            is_active = (i == engine.active_reference)
            
            if is_active:
                pygame.draw.rect(surface, config.COLORS["button_active"], btn_rect, border_radius=4)
            elif is_hover:
                pygame.draw.rect(surface, config.COLORS["button_hover"], btn_rect, border_radius=4)
                
            text_color = config.COLORS["text_highlight"] if is_active else config.COLORS["text"]
            text_surf = self.font_nav.render(ref["title"], True, text_color)
            surface.blit(text_surf, (btn_rect.x + 15, btn_rect.y + 8))
            
            y_offset += 40
            
        # Draw close button
        close_hover = self.close_rect.collidepoint(mouse_pos)
        pygame.draw.rect(surface, (200, 50, 50) if close_hover else (150, 50, 50), self.close_rect, border_radius=4)
        close_text = self.font_header.render("X", True, (255, 255, 255))
        surface.blit(close_text, (self.close_rect.x + 8, self.close_rect.y + 3))

        # Draw content pane (Right)
        data = REFERENCES_DATA[engine.active_reference]
        content_pad = 40
        cx = self.content_rect.x + content_pad
        cy = self.content_rect.y + content_pad
        cw = self.content_rect.width - content_pad * 2
        
        # Title
        title_surf = self.font_title.render(data["title"], True, config.COLORS["text_highlight"])
        surface.blit(title_surf, (cx, cy))
        cy += 50
        
        # Helper to draw sections
        def draw_section(title, text, y_pos):
            if not text: return y_pos
            header_surf = self.font_header.render(title, True, config.COLORS["highlight"])
            surface.blit(header_surf, (cx, y_pos))
            y_pos += 30
            text_rect = pygame.Rect(cx, y_pos, cw, 1000)
            h = self.draw_text_wrapped(surface, text, self.font_body, config.COLORS["text"], text_rect)
            return y_pos + h + 25

        cy = draw_section("Theory", data.get("theory", ""), cy)
        cy = draw_section("Key Insight", data.get("insight", ""), cy)
        
        if "euclidean" in data or "hyperbolic" in data:
            header_surf = self.font_header.render("Geometry Comparison", True, config.COLORS["highlight"])
            surface.blit(header_surf, (cx, cy))
            cy += 30
            if "euclidean" in data:
                text_rect = pygame.Rect(cx + 10, cy, cw - 10, 1000)
                h = self.draw_text_wrapped(surface, "• Euclidean: " + data["euclidean"], self.font_body, config.COLORS["e_line"], text_rect)
                cy += h + 15
            if "hyperbolic" in data:
                text_rect = pygame.Rect(cx + 10, cy, cw - 10, 1000)
                h = self.draw_text_wrapped(surface, "• Hyperbolic: " + data["hyperbolic"], self.font_body, config.COLORS["h_line"], text_rect)
                cy += h + 25

        if data.get("author"):
            cy = draw_section("Contributors", data["author"], cy)

    def handle_click(self, pos, engine):
        if self.close_rect.collidepoint(pos):
            engine.show_references = False
            return True
            
        nav_rect = pygame.Rect(self.rect.left, self.rect.top, self.nav_width, self.rect.height)
        if nav_rect.collidepoint(pos):
            y_offset = nav_rect.y + 60
            for i in range(len(REFERENCES_DATA)):
                btn_rect = pygame.Rect(nav_rect.x + 10, y_offset, nav_rect.width - 20, 35)
                if btn_rect.collidepoint(pos):
                    engine.active_reference = i
                    return True
                y_offset += 40
                
        # If clicked outside the modal, close it
        if not self.rect.collidepoint(pos):
            engine.show_references = False
            return True
            
        return True # Handled click (even if on empty modal space)

def auto_select_reference_for_tool(engine):
    for i, ref in enumerate(REFERENCES_DATA):
        if ref.get("tool_link") == engine.tool:
            engine.active_reference = i
            break
