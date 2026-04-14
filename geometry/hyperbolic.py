import math

def hyperbolic_distance(p1, p2):
    """
    Computes hyperbolic distance in the Poincare disk model.
    d = cosh^-1 (1 + (2|p-q|^2) / ((1-|p|^2)(1-|q|^2)))
    """
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dist_sq = dx**2 + dy**2
    
    mag1_sq = p1[0]**2 + p1[1]**2
    mag2_sq = p2[0]**2 + p2[1]**2
    
    denom = (1 - mag1_sq) * (1 - mag2_sq)
    if denom <= 0:
        return float('inf') # point on the boundary
        
    val = 1 + (2 * dist_sq) / denom
    if val < 1:
        val = 1
    return math.acosh(val)

def get_geodesic_arc(p1, p2):
    """
    Returns either ('line', p1, p2) if points are collinear with origin,
    or ('arc', center_x, center_y, radius, angle1, angle2) for rendering.
    Points and outputs are in logical coordinates [-1, 1].
    """
    cross_prod = p1[0]*p2[1] - p1[1]*p2[0]
    # Check if collinear with origin
    if abs(cross_prod) < 1e-6:
        return ('line', p1, p2)
        
    mag1_sq = p1[0]**2 + p1[1]**2
    if mag1_sq < 1e-6:
        return ('line', p1, p2)
        
    # Inversion of p1 w.r.t unit circle
    p1_inv = (p1[0] / mag1_sq, p1[1] / mag1_sq)
    
    def perp_bisector(a, b):
        mx = (a[0] + b[0]) / 2
        my = (a[1] + b[1]) / 2
        vx = b[1] - a[1]
        vy = -(b[0] - a[0])
        return mx, my, vx, vy
        
    m1x, m1y, v1x, v1y = perp_bisector(p1, p2)
    m2x, m2y, v2x, v2y = perp_bisector(p1, p1_inv)
    
    det = v1x * v2y - v1y * v2x
    if abs(det) < 1e-6:
        return ('line', p1, p2)
        
    t = ((m2x - m1x)*v2y - (m2y - m1y)*v2x) / det
    
    cx = m1x + t * v1x
    cy = m1y + t * v1y
    r = math.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    
    ang1 = math.atan2(p1[1] - cy, p1[0] - cx)
    ang2 = math.atan2(p2[1] - cy, p2[0] - cx)
    
    # Ensure correct rendering order based on angles
    return ('arc', cx, cy, r, ang1, ang2)

def hyperbolic_triangle_angles(p1, p2, p3):
    """
    Returns (angle_at_p1, angle_at_p2, angle_at_p3) in degrees.
    Using hyperbolic law of cosines: cosh c = cosh a cosh b - sinh a sinh b cos C
    """
    a = hyperbolic_distance(p2, p3)
    b = hyperbolic_distance(p1, p3)
    c = hyperbolic_distance(p1, p2)
    
    def angle(adj1, adj2, opp):
        try:
            sinh1 = math.sinh(adj1)
            sinh2 = math.sinh(adj2)
            if sinh1 == 0 or sinh2 == 0:
                return 0
            val = (math.cosh(adj1) * math.cosh(adj2) - math.cosh(opp)) / (sinh1 * sinh2)
            val = max(min(val, 1.0), -1.0)
            return math.degrees(math.acos(val))
        except (ValueError, ZeroDivisionError, OverflowError):
            return 0
            
    angle_p1 = angle(b, c, a)
    angle_p2 = angle(a, c, b)
    angle_p3 = angle(a, b, c)
    
    return angle_p1, angle_p2, angle_p3

def get_hyperbolic_parallels(l_p1, l_p2, p, num_lines=7):
    base = get_geodesic_arc(l_p1, l_p2)
    
    valid_pts = []
    
    for i in range(100):
        theta = (i / 100) * math.pi
        eps = 0.05
        p_cand = (p[0] + eps * math.cos(theta), p[1] + eps * math.sin(theta))
        
        # Test bounds
        if p_cand[0]**2 + p_cand[1]**2 > 0.99**2:
            continue
            
        cand = get_geodesic_arc(p, p_cand)
        
        intersects = False
        
        if base[0] == 'line' and cand[0] == 'line':
            intersects = True
        elif base[0] == 'line':
            # candidate is arc
            cx, cy, r = cand[1], cand[2], cand[3]
            # base line goes through origin
            bx, by = l_p2[0]-l_p1[0], l_p2[1]-l_p1[1]
            dist_num = abs(by * cx - bx * cy)
            dist_den = math.sqrt(bx**2 + by**2)
            if dist_den > 0 and dist_num / dist_den < r:
                intersects = True
        elif cand[0] == 'line':
            # base is arc
            cx, cy, r = base[1], base[2], base[3]
            bx, by = p_cand[0]-p[0], p_cand[1]-p[1]
            dist_num = abs(by * cx - bx * cy)
            dist_den = math.sqrt(bx**2 + by**2)
            if dist_den > 0 and dist_num / dist_den < r:
                intersects = True
        else:
            # both arcs
            cx1, cy1, r1 = base[1], base[2], base[3]
            cx2, cy2, r2 = cand[1], cand[2], cand[3]
            d = math.sqrt((cx1-cx2)**2 + (cy1-cy2)**2)
            if abs(r1 - r2) < d < r1 + r2:
                intersects = True
                
        if not intersects:
            valid_pts.append(cand)
            
    # Sample uniformly from valid arcs
    # Note: Valid ones are typically contiguous in theta
    if not valid_pts:
        return []
        
    step = max(1, len(valid_pts) // min(num_lines, len(valid_pts)))
    selected = valid_pts[::step][:num_lines]
    
    return selected

