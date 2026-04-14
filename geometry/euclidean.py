import math
from utils.math_utils import distance

def euclidean_distance(p1, p2):
    return distance(p1[0], p1[1], p2[0], p2[1])

def euclidean_triangle_angles(p1, p2, p3):
    """
    Returns (angle_at_p1, angle_at_p2, angle_at_p3) in degrees.
    Based on cosine rule: c^2 = a^2 + b^2 - 2ab*cos(C)
    """
    a = euclidean_distance(p2, p3)
    b = euclidean_distance(p1, p3)
    c = euclidean_distance(p1, p2)
    
    def angle(adj1, adj2, opp):
        if adj1 == 0 or adj2 == 0:
            return 0
        cos_theta = (adj1**2 + adj2**2 - opp**2) / (2 * adj1 * adj2)
        cos_theta = max(min(cos_theta, 1.0), -1.0)
        return math.degrees(math.acos(cos_theta))
        
    angle_p1 = angle(b, c, a)
    angle_p2 = angle(a, c, b)
    angle_p3 = angle(a, b, c)
    
    return angle_p1, angle_p2, angle_p3

def get_euclidean_parallel(l_p1, l_p2, p):
    dx = l_p2[0] - l_p1[0]
    dy = l_p2[1] - l_p1[1]
    
    # Scale by a large factor to extend across the drawing bounds
    p_end1 = (p[0] - dx * 2, p[1] - dy * 2)
    p_end2 = (p[0] + dx * 2, p[1] + dy * 2)
    return p_end1, p_end2
