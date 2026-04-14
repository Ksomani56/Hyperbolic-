Here’s a clean **`upgrade.md`** you can directly give to Antigravity 👇

---

# 📄 upgrade.md

## Dual Geometry Visualizer — Feature Expansion Plan

---

# 🎯 Purpose

This document defines **post-MVP enhancements** to elevate the project from a functional visualizer to a **high-impact educational and demo tool**.

Focus:

* Better understanding of non-Euclidean geometry
* Stronger visual storytelling
* Improved interaction and usability

---

# 🧠 Feature Roadmap

---

# 🟢 TIER 1 — High Impact, Low Complexity (Priority)

## 1. Live Measurement Overlay

### Description:

Display real-time geometric values when objects are selected.

### Requirements:

* Show:

  * Distance (Euclidean vs Hyperbolic)
  * Angle values
  * Triangle angle sum
* Dynamic updates when points move

### Goal:

Make the system feel analytical, not just visual.

---

## 2. Snap-to-Grid / Precision Mode

### Description:

Enable precise point placement.

### Requirements:

* Toggle grid (Euclidean panel)
* Snap points to nearest grid intersection
* Adjustable grid density (optional)

---

## 3. Geodesic Highlighting

### Description:

Clarify differences between geometries.

### Requirements:

* Hover over line:

  * Highlight corresponding line in both panels
* Display label:

  * “Geodesic (shortest path in this geometry)”

---

## 4. Preset Demonstrations

### Description:

Prebuilt examples for quick demonstrations.

### Presets:

* Hyperbolic Triangle
* Parallel Lines
* Boundary Distortion

### Requirement:

* One-click generation
* Fully interactive after generation

---

# 🟡 TIER 2 — Conceptual Features (Medium Priority)

## 5. Triangle Area Comparison

### Description:

Compare areas in both geometries.

### Requirements:

* Compute and display:

  * Euclidean area
  * Hyperbolic area (approximation acceptable)
* Show how area changes near boundary

---

## 6. Boundary Behavior Visualization

### Description:

Demonstrate distortion near disk boundary.

### Requirements:

* Drag point toward edge:

  * Show increasing hyperbolic distance
  * Visual shrink/compression
* Optional:

  * Display scaling factor

### Insight:

Represents infinite space inside finite boundary.

---

## 7. Transformations (Move/Rotate)

### Description:

Apply transformations to shapes.

### Requirements:

* Translate objects
* Rotate objects
* Show:

  * Euclidean → rigid motion
  * Hyperbolic → distortion

---

## 8. Path Animation

### Description:

Animate shortest path between points.

### Requirements:

* Select two points
* Animate:

  * Euclidean straight line traversal
  * Hyperbolic curved geodesic traversal

---

# 🔴 TIER 3 — Advanced / Showcase Features

## 9. Tessellation Generator

### Description:

Generate repeating geometric patterns.

### Requirements:

* Create tiling inside Poincaré disk
* Shapes shrink toward boundary
* Adjustable density

### Goal:

Strong visual impact for demos

---

## 10. Theorem Proof Mode

### Description:

Guided, step-by-step explanations.

### Example:

Triangle Angle Sum:

1. Draw triangle
2. Display angles
3. Show total < 180°

### Requirements:

* Step navigation
* Text explanation overlays

---

## 11. Multiple Model Support (Advanced)

### Description:

Support different hyperbolic models.

### Models:

* Poincaré Disk (existing)
* Klein Model (optional)

### Requirement:

* Toggle between models
* Same input, different representation

---

## 12. Data Panel

### Description:

Display system-level statistics.

### Metrics:

* Number of objects
* Total geodesic length
* Average distortion factor

---

# 🔵 TIER 4 — UX & Polish

## 13. Color Encoding

### Standard:

* Euclidean → Blue
* Hyperbolic → Red

---

## 14. Dark Mode

### Requirements:

* Toggle theme
* Maintain contrast and readability

---

## 15. Smart Selection System

### Features:

* Click to select object
* Highlight selection
* Show properties panel

---

## 16. Export Functionality

### Options:

* Export screenshot (PNG)
* Export geometry data (JSON)

---

# ⚠️ Constraints

* Do NOT implement full physical hyperbolic simulation
* Maintain performance ≥ 30 FPS
* Avoid UI clutter
* Prioritize clarity over mathematical completeness

---

# 🧪 Success Criteria

The upgraded system should:

* Clearly demonstrate:

  * Curved geodesics
  * Triangle angle deviation
  * Distance distortion
* Allow users to:

  * Interact intuitively
  * Understand differences without external explanation

---

# 🏁 Final Note

Enhancements should **reinforce understanding**, not just add complexity.

Every feature must answer:

> “Does this help the user *see* or *understand* geometry better?”

If not, it should not be included.

---
