Sidebar Module — References & Theory
🎯 Purpose

Provide users with authentic theoretical context behind each visual demonstration.

This ensures:

Conceptual clarity
Academic credibility
Stronger viva/hackathon impact
🧠 Feature Overview

Add a “References” section in the sidebar where users can:

Read the theory behind each module
See the original contributors / mathematicians
Understand why the visual behavior occurs
🖥️ UI/UX REQUIREMENTS
1. Sidebar Section
Label:

📚 References

2. Structure
References
│
├── Parallel Postulate
├── Triangle Angle Sum
├── Hyperbolic Geometry Basics
├── Geodesics
├── Distance Formula
3. Interaction
Click on a topic → opens:
Expandable panel OR modal
Display:
Explanation
Author / Mathematician
Key insight
📖 CONTENT REQUIREMENTS

Each reference must include:

1. Title
2. Short Explanation (2–4 lines)
3. Key Insight
4. Author / Contributor
📚 REFERENCE CONTENT (READY TO USE)
🧠 1. Parallel Postulate

Theory:
Through a point not on a line, the number of parallel lines depends on the geometry.

Euclidean Insight:
Exactly one parallel exists.

Hyperbolic Insight:
Infinitely many parallels exist.

Author:
Euclid, challenged by Nikolai Lobachevsky and János Bolyai

🧠 2. Triangle Angle Sum

Theory:
The sum of angles in a triangle depends on curvature.

Euclidean:
Sum = 180°

Hyperbolic:
Sum < 180°

Insight:
Angle defect reflects curvature.

Contributor:
Carl Friedrich Gauss

🧠 3. Hyperbolic Geometry

Theory:
A geometry with constant negative curvature.

Insight:
Space expands faster than Euclidean space.

Contributor:
Nikolai Lobachevsky

🧠 4. Geodesics

Theory:
Shortest path between two points.

Euclidean:
Straight line

Hyperbolic:
Curved arcs (in Poincaré disk)

Contributor:
Bernhard Riemann

🧠 5. Distance in Hyperbolic Space

Theory:
Distance increases rapidly near boundary.

Insight:
Boundary represents infinity.

Contributor:
Henri Poincaré

🧠 6. Circle Growth

Theory:
Circumference grows faster than 
2
𝜋
𝑟
2πr in hyperbolic space.

Insight:
Indicates exponential expansion of space.

🧠 7. Tessellation

Theory:
Infinite tiling possible due to negative curvature.

Contributor:
M. C. Escher

🎛️ FUNCTIONAL REQUIREMENTS
Scrollable reference panel
Lightweight text (no heavy rendering)
Works alongside Explain Mode
✨ OPTIONAL ENHANCEMENTS
🔗 1. Link to Active Module
When user selects a theorem → auto-highlight reference
🎧 2. “Explain This” Button
Click → shows theory related to current action
🧾 3. Expand / Collapse Sections
Keep UI clean
⚠️ CONSTRAINTS
Keep explanations concise (no long paragraphs)
Avoid academic overload
Focus on intuition + clarity
🧪 SUCCESS CRITERIA

User should be able to:

Understand what is happening visually
Understand why it is happening
Recognize key contributors in geometry
🏁 FINAL NOTE

This feature transforms your project from:
👉 “Visualization tool”
to
👉 “Interactive geometry textbook”