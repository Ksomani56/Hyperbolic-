Here’s a **clean, execution-ready PRD** you can hand to Antigravity. It’s structured like something a real product/engineering team would use—clear scope, constraints, and deliverables.

---

# 📄 Product Requirements Document (PRD)

## 🧩 Project Title

**Dual Geometry Visualizer (Euclidean vs Non-Euclidean)**

---

## 🎯 Objective

Build an **interactive educational visualization tool** that demonstrates the differences between Euclidean and hyperbolic geometry using a **split-screen interface**.

Users will:

* Draw geometric objects in Euclidean space
* See **real-time transformed equivalents** in hyperbolic space (Poincaré disk model)
* Interactively explore and validate geometric properties

---

## 👥 Target Users

* Engineering students (Computer Graphics / Math)
* Professors (teaching tool)
* Hackathon judges (demo-focused audience)

---

## 🧠 Core Concept

> Same input → different geometry → different results

Left side = Euclidean
Right side = Hyperbolic (Poincaré Disk)

---

## 🖥️ UI/UX REQUIREMENTS

## 1. Layout

```
 -----------------------------------------------------
| Sidebar | Euclidean Plane | Hyperbolic Disk         |
|         | (Left Panel)    | (Right Panel)           |
 -----------------------------------------------------
```

---

## 2. Sidebar (Control Panel)

### Sections:

**A. Drawing Tools**

* Point Tool
* Line Tool
* Triangle Tool (Phase 2)

**B. Geometry Mode**

* Euclidean (default)
* Hyperbolic (visualized automatically)

**C. Actions**

* Undo
* Clear
* Playback

**D. Theorem Demos**

* Triangle Angle Sum
* Parallel Lines
* Distance Tool

**E. Toggle**

* Explain Mode (ON/OFF)

---

## 🖱️ INTERACTION MODEL

### Mouse Controls:

* **Left Click** → Add point
* **Select 2 points** → Draw line
* **Hover** → Show coordinates

---

## 🔁 SYNCHRONIZATION LOGIC

All actions occur in Euclidean space and are **mirrored** into hyperbolic space.

### Object Mapping:

| Object   | Euclidean      | Hyperbolic                 |
| -------- | -------------- | -------------------------- |
| Point    | (x, y)         | Same normalized coordinate |
| Line     | Straight line  | Geodesic (arc or diameter) |
| Triangle | Straight edges | Curved edges               |

---

## 🧮 MATHEMATICAL MODEL

### Hyperbolic Space Representation:

* **Poincaré Disk Model**
* Unit circle boundary

### Geodesics:

* Diameter OR
* Circular arcs perpendicular to boundary

### Distance (Phase 2):

[
d = \cosh^{-1} \left(1 + \frac{2|p-q|^2}{(1-|p|^2)(1-|q|^2)}\right)
]

---

## 🎬 PLAYBACK SYSTEM

### Requirement:

Record all user actions and replay sequentially.

### Action Log Format:

```json
[
  {"type": "add_point", "x": 0.3, "y": 0.2},
  {"type": "draw_line", "p1": 0, "p2": 1}
]
```

### Playback Behavior:

* Step-by-step animation
* Adjustable speed (optional)

---

## 🧪 FEATURE MODULES

## 1. Split-Screen Visualization (HIGH PRIORITY)

* Left: Cartesian grid
* Right: Unit disk

---

## 2. Geodesic Rendering (HIGH PRIORITY)

* Compute circle or diameter
* Clip within disk

---

## 3. Triangle Angle Sum Demo (HIGH PRIORITY)

* User draws triangle
* System calculates angles

### Output:

* Euclidean → ~180°
* Hyperbolic → < 180°

---

## 4. Parallel Lines Demo (MEDIUM PRIORITY)

* Draw base line
* Show multiple “parallel” lines

---

## 5. Distance Tool (MEDIUM PRIORITY)

* Click two points
* Display:

  * Euclidean distance
  * Hyperbolic distance

---

## 6. Explain Mode (HIGH IMPACT)

When enabled:

* Show contextual tooltips:

  * “This is a geodesic”
  * “Angles preserved, distances distorted”

---

## 🧱 TECH STACK

### Language:

* Python 3.x

### Libraries:

* `pygame` → rendering & interaction
* `numpy` → math
* optional: `matplotlib` (debugging)

---

## 🏗️ SYSTEM ARCHITECTURE

```
/project
│
├── main.py
├── config.py
│
├── geometry/
│   ├── euclidean.py
│   ├── hyperbolic.py
│
├── core/
│   ├── objects.py      # Point, Line, Triangle
│   ├── engine.py       # sync logic
│   ├── playback.py
│
├── ui/
│   ├── renderer.py
│   ├── input_handler.py
│   ├── sidebar.py
│
└── utils/
    ├── math_utils.py
```

---

## ⚡ PERFORMANCE REQUIREMENTS

* Real-time interaction (≥ 30 FPS)
* Smooth rendering of arcs
* No lag on up to 50 objects

---

## 🚫 CONSTRAINTS

* Do NOT implement full hyperbolic physics
* Visualization accuracy > physical simulation
* Focus on clarity over complexity

---

## 🧪 SUCCESS METRICS

* User can:

  * Draw points and lines easily
  * See immediate transformation
  * Understand at least 2 geometric differences

* Demo should clearly show:

  * Triangle angle deviation
  * Curved geodesics

---

## 🎯 MVP SCOPE (STRICT)

Must include:

* Split screen
* Point + line drawing
* Hyperbolic geodesics
* Playback
* Triangle demo

---

## 🚀 FUTURE EXTENSIONS

* Circle inversion
* Tessellation patterns
* 3D hyperbolic visualization
* Export drawings

---

## 🎤 DEMO SCRIPT (FOR PRESENTATION)

1. Draw two points → connect
2. Show straight vs curved
3. Draw triangle
4. Show angle sum difference
5. Playback demonstration

---

## ⚠️ RISKS

| Risk         | Mitigation                    |
| ------------ | ----------------------------- |
| Complex math | Use simplified geodesic model |
| UI clutter   | Minimalist sidebar            |
| Sync bugs    | Central engine logic          |

---

## ✅ FINAL NOTE FOR ANTIGRAVITY

Focus on:

* Clean UI
* Accurate geodesic rendering
* Smooth interaction

Avoid overengineering.

---

