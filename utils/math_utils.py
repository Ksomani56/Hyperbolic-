import math
import numpy as np

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def angle_between_lines(p1, p2, p3):
    """
    Angle at p2 internally formed by lines p1-p2 and p3-p2.
    Returns angle in degrees.
    """
    v1 = (p1[0] - p2[0], p1[1] - p2[1])
    v2 = (p3[0] - p2[0], p3[1] - p2[1])
    
    dot_prod = v1[0]*v2[0] + v1[1]*v2[1]
    mag1 = distance(v1[0], v1[1], 0, 0)
    mag2 = distance(v2[0], v2[1], 0, 0)
    
    if mag1 == 0 or mag2 == 0:
        return 0
        
    cos_theta = dot_prod / (mag1 * mag2)
    # Handle floating point inaccuracies
    cos_theta = max(min(cos_theta, 1.0), -1.0)
    
    return math.degrees(math.acos(cos_theta))

def normalize_point(x, y, rect, render_scale=1.0, invert_y=True):
    """
    Transforms screen space coordinates to logical space [-1, 1].
    Origin (0,0) is at the center of the rect.
    """
    rx, ry, rw, rh = rect
    cx, cy = rx + rw/2, ry + rh/2
    
    scale = (min(rw, rh) / 2) * render_scale
    
    nx = (x - cx) / scale
    ny = (y - cy) / scale
    
    if invert_y:
        ny = -ny
        
    return nx, ny

def denormalize_point(nx, ny, rect, render_scale=1.0, invert_y=True):
    """
    Transforms logical space [-1, 1] to screen space coordinates.
    """
    rx, ry, rw, rh = rect
    cx, cy = rx + rw/2, ry + rh/2
    
    scale = (min(rw, rh) / 2) * render_scale
    
    if invert_y:
        ny = -ny
        
    sx = nx * scale + cx
    sy = ny * scale + cy
    
    return sx, sy

def point_line_distance(px, py, l1x, l1y, l2x, l2y):
    """
    Returns distance from point (px, py) to line segment ((l1x, l1y), (l2x, l2y))
    """
    line_mag = distance(l1x, l1y, l2x, l2y)
    if line_mag < 1e-6:
        return distance(px, py, l1x, l1y)
        
    u1 = (((px - l1x) * (l2x - l1x)) + ((py - l1y) * (l2y - l1y)))
    u = u1 / (line_mag * line_mag)
    
    if u < 0.0 or u > 1.0:
        d1 = distance(px, py, l1x, l1y)
        d2 = distance(px, py, l2x, l2y)
        return min(d1, d2)
        
    ix = l1x + u * (l2x - l1x)
    iy = l1y + u * (l2y - l1y)
    return distance(px, py, ix, iy)
