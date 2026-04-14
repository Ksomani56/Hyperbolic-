Animated Line Drawing for Playback System
🎯 Purpose

Enhance the playback system by introducing progressive line rendering, allowing users to visually observe how geometric constructions are formed step-by-step.

This feature improves:

Conceptual understanding
Visual clarity
Demo quality
🧠 Feature Overview

When the user clicks “Play Actions”:

Points appear sequentially
Lines are drawn gradually over time
Animation follows the actual geometric path:
Euclidean → straight line
Hyperbolic → curved geodesic
⚙️ Functional Requirements
1. Progressive Line Rendering
Behavior:
Lines should not appear instantly
They should “grow” from start point → end point
2. Geometry-Specific Animation
A. Euclidean Lines
Linear interpolation between two points
B. Hyperbolic Geodesics
Animate along arc (or diameter)
Must follow computed geodesic path
3. Playback Integration
Action Format Update:
{
  "type": "draw_line",
  "p1": 0,
  "p2": 1,
  "animated": true
}
4. Frame-Based Animation
Progress Variable:
Range: 0 → 1
Controls how much of the line is drawn
Update Rule:
progress += speed
Clamp at 1.0
🧮 Implementation Details
1. Euclidean Line Animation
Interpolation:
x = x1 + t * (x2 - x1)
y = y1 + t * (y2 - y1)
Rendering:
Draw line from (x1, y1) to (x_current, y_current)
2. Hyperbolic Geodesic Animation
Inputs:
Center (h, k)
Radius r
Start angle θ1
End angle θ2
Interpolation:
θ_current = θ1 + t * (θ2 - θ1)
Rendering:
Generate points from θ1 → θ_current
Draw partial arc
3. Sampling Resolution
Minimum: 100 points per arc
Should scale with arc length
Avoid jagged rendering
4. Geometry Caching
Requirement:
Compute geodesic parameters once
Store:
Center
Radius
Angles
Reason:

Avoid recomputation every frame (performance optimization)

🎛️ Controls & UI Requirements
1. Playback Controls
▶ Play
⏸ Pause
⏭ Resume
2. Speed Control
Adjustable animation speed
Suggested presets:
Slow (demo mode)
Medium
Fast
✨ Visual Enhancements
1. Drawing Indicator
Use a distinct color during animation (e.g., yellow)
Final color after completion:
Euclidean → Blue
Hyperbolic → Red
2. Animated Tip
Highlight current drawing endpoint
Optional glow effect
3. Fade-In Effect (Optional)
Slight opacity increase as line completes
🧠 Motion Enhancement (Optional but Recommended)
Easing Function

Instead of linear animation:

progress = 1 - (1 - t)**2
Effect:
Smooth start
Natural acceleration
Better visual feel
🧱 System Integration
Module: playback.py
Responsibilities:
Iterate through action list
Trigger animations
Manage progress state
Module: renderer.py
Responsibilities:
Render partial lines
Handle arc drawing
Data Flow:
Action → Playback Engine → Animation State → Renderer → Frame Output
⚡ Performance Requirements
Maintain ≥ 30 FPS
Smooth animation without stutter
Efficient handling of multiple simultaneous objects
⚠️ Constraints
Do not recompute geometry per frame
Avoid full redraw masking techniques
Keep animation consistent across both geometries
🧪 Success Criteria
Lines visibly “grow” during playback
Hyperbolic arcs animate smoothly and correctly
User can clearly understand construction steps
No noticeable lag or frame drops
🏁 Final Note

This feature is not just visual polish — it is a core explanatory tool.

It should make users feel:

“I can see how this geometry is being constructed.”