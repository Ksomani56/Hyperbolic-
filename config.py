# Window dimensions
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

# Layout configurations (split screen logic)
SIDEBAR_WIDTH = 250
SIDEBAR_RECT = (0, 0, SIDEBAR_WIDTH, WINDOW_HEIGHT)

# Euclidean panel (left panel)
EUCLIDEAN_WIDTH = (WINDOW_WIDTH - SIDEBAR_WIDTH) // 2
EUCLIDEAN_HEIGHT = WINDOW_HEIGHT
EUCLIDEAN_RECT = (SIDEBAR_WIDTH, 0, EUCLIDEAN_WIDTH, EUCLIDEAN_HEIGHT)

# Hyperbolic panel (right panel)
HYPERBOLIC_WIDTH = EUCLIDEAN_WIDTH
HYPERBOLIC_HEIGHT = WINDOW_HEIGHT
HYPERBOLIC_RECT = (SIDEBAR_WIDTH + EUCLIDEAN_WIDTH, 0, HYPERBOLIC_WIDTH, HYPERBOLIC_HEIGHT)

# Colors (RGB)
COLORS = {
    "background": (18, 18, 18),
    "panel_bg": (24, 24, 24),
    "grid": (42, 42, 42),
    "border": (42, 42, 42),
    "text": (200, 200, 200),
    "text_highlight": (255, 255, 255),
    "e_point": (77, 163, 255),
    "e_line": (77, 163, 255),
    "e_triangle": (77, 163, 255),
    "h_point": (255, 107, 107),
    "h_line": (255, 107, 107),
    "h_triangle": (255, 107, 107),
    "highlight": (255, 255, 255),
    "sidebar_bg": (26, 26, 26),
    "button_bg": (31, 31, 31),
    "button_hover": (42, 42, 42),
    "button_active": (47, 128, 237),
    "button_disabled": (85, 85, 85),
    "tooltip_bg": (31, 31, 31),
    "tooltip_text": (200, 200, 200),
    "disk_bg": (234, 234, 234),
}

# FPS setup
FPS = 60

# Point render size
POINT_RADIUS = 5
LINE_WIDTH = 2

# Model configurations
# Logical range for coordinate mappings x, y from -1 to 1
LOGICAL_BOUND = 1.0
DISK_RADIUS_RATIO = 0.9  # Use 90% of the half-width

# Grid settings
GRID_STEP = 0.1
