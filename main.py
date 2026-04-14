import pygame
import sys
import config
from core.engine import Engine
from ui.sidebar import Sidebar
from ui.input_handler import InputHandler
from ui.renderer import Renderer
from ui.references import ReferencesModal

def main():
    pygame.init()
    
    # Initialize display
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption("Dual Geometry Visualizer (Euclidean vs Non-Euclidean)")
    clock = pygame.time.Clock()
    
    # Initialize components
    engine = Engine()
    sidebar = Sidebar()
    renderer = Renderer(screen)
    ref_modal = ReferencesModal()
    input_handler = InputHandler(engine, sidebar, ref_modal)
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        
        # Handle input
        running = input_handler.handle_events()
        
        # Update logic
        engine.update(current_time)
        
        # Render
        renderer.draw(engine)
        sidebar.draw(screen, pygame.mouse.get_pos(), engine)
        
        if engine.show_references:
            ref_modal.draw(screen, engine, pygame.mouse.get_pos())
        
        pygame.display.flip()
        clock.tick(config.FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
