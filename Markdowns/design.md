📄 design.md
Dual Geometry Visualizer — UI Design System
🎯 Design Philosophy

The interface should feel like:

A modern mathematical lab — clean, minimal, and focused on insight

Key principles:

Clarity over decoration
Strong visual hierarchy
Subtle but intentional color usage
Geometry is the hero, UI stays secondary
🎨 Color System
Core Colors
Element	Color	Usage
Background	#121212	Main app background
Sidebar	#1A1A1A	Slight contrast
Panels	#181818	Drawing areas
Border/Divider	#2A2A2A	Subtle separation
Geometry Colors
Geometry Type	Color
Euclidean	#4DA3FF (Blue)
Hyperbolic	#FF6B6B (Red)
Accent Colors
State	Color
Active Button	#2F80ED
Hover	#2A2A2A
Disabled	#555555
🧱 Layout System
Structure
 -----------------------------------------------------
| Sidebar | Euclidean Panel | Hyperbolic Panel        |
 -----------------------------------------------------
Sidebar Width
Fixed: 220–260px
Panel Split
Equal width (50% / 50%)
Padding
Global: 12–16px
Section gaps: 20–24px
🧩 Sidebar Design
Section Grouping
TOOLS
Point Tool
Line Tool
DEMOS
Triangle Demo
Parallel Demo
Distance Demo
ACTIONS
Undo
Clear
▶ Play
SETTINGS
Explain Mode
Snap to Grid
EXTRAS
📚 References
Button Design
Base Style
Background: #1F1F1F
Border: none
Radius: 10px
Padding: 10–12px
States
State	Style
Default	Dark grey
Hover	Slightly lighter
Active	Accent color + subtle glow
Pressed	Slight scale (0.98x)
Typography
Font: Inter / SF Pro / Roboto
Title: Bold
Buttons: Medium
Size:
Title: 16–18px
Buttons: 13–14px
🖥️ Canvas Panels
Euclidean Panel
Features:
Light grid (very subtle)
X and Y axis highlighted
Colors:
Grid: #2A2A2A
Axis: #4DA3FF
Hyperbolic Panel
Features:
Dark background
Poincaré disk centered
Disk Styling:
Fill: #EAEAEA (NOT pure white)
Border: subtle grey
Optional:
Radial grid (low opacity)
✨ Visual Enhancements
1. Line Styling
Type	Style
Euclidean	Blue, solid
Hyperbolic	Red, smooth arc
2. Animation
Lines draw progressively
Slight glow during drawing
Smooth easing (not linear)
3. Selection Feedback
Selected object:
Slight glow
Increased thickness
4. Hover Effects
Highlight object under cursor
Show coordinates tooltip
🎛️ Playback UI
Button
Icon: ▶
Changes to ⏸ when playing
Progress Indicator
Thin bar below canvas
Color: accent
📚 References Panel
Behavior:
Opens as:
Slide-in panel OR modal
Style:
Background: #1A1A1A
Text: light grey
Section headings: bold
🧠 Explain Mode
Behavior:
Show contextual text overlays
Style:
Semi-transparent background
Small text box near object
📏 Spacing Rules
Between buttons: 10–12px
Between sections: 20–24px
Panel padding: 12–16px
⚡ Performance Considerations
Avoid heavy shadows
Use minimal gradients
Prefer flat design
⚠️ Constraints
Do NOT overcrowd UI
Do NOT use more than 3–4 main colors
Do NOT reduce canvas size excessively
🧪 Success Criteria

UI should feel:

Clean
Modern
Focused

User should:

Instantly understand layout
Easily differentiate geometries
Focus on visualization, not controls
🏁 Final Note

The UI should not compete with the geometry.

It should quietly support it.