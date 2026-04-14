Here’s a clean, structured **`upgrades.md`** you can hand to Antigravity 👇

---

# 📄 upgrades.md

## UI Enhancements — Dual Geometry Visualizer

---

# 🎯 Purpose

Upgrade the current UI from a functional layout to a **polished, demo-ready visualization system**.

Focus areas:

* Visual hierarchy
* Concept clarity (Euclidean vs Hyperbolic)
* Canvas dominance
* Subtle but impactful design improvements

---

# 🧠 Current Issues

## 1. Lack of Visual Differentiation

* Euclidean and Hyperbolic panels look identical
* No visual indication of different geometries

---

## 2. Empty Canvas Feel

* No grid or axes
* Panels lack structure and context

---

## 3. Hyperbolic Disk Looks Flat

* Pure white fill feels disconnected
* No depth or integration

---

## 4. Sidebar Dominance

* Sidebar visually heavier than canvas
* Draws attention away from geometry

---

## 5. Weak Titles & Labels

* “Euclidean Space” / “Hyperbolic Space” lack emphasis
* No contextual meaning

---

## 🚀 REQUIRED UI IMPROVEMENTS

---

# 🧩 1. Differentiate Geometry Panels (HIGH PRIORITY)

## Euclidean Panel

### Add:

* Subtle grid
* Slight blue tint

### Styling:

```css
background: #0f1720;
grid color: rgba(77,163,255,0.08);
```

---

## Hyperbolic Panel

### Add:

* Darker background
* Radial gradient

### Styling:

```css
background: radial-gradient(circle, #141414 40%, #0f0f0f 100%);
```

---

## Goal:

* Left → structured, flat
* Right → curved, organic

---

# 🎨 2. Improve Hyperbolic Disk (HIGH PRIORITY)

## Changes:

* Replace pure white with softer tone:

```css
fill: #E6E6E6;
```

* Add subtle edge + glow:

```css
border: 1px solid rgba(255,255,255,0.2);
box-shadow: 0 0 40px rgba(255,255,255,0.05);
```

---

## Goal:

Make disk feel like a **space**, not a flat object

---

# 📏 3. Add Grid & Axes (HIGH PRIORITY)

## Euclidean Panel:

* X and Y axes
* Light grid lines

## Hyperbolic Panel (Optional but recommended):

* Radial lines
* Concentric circles

---

## Goal:

Remove empty feel and provide spatial context

---

# 🧠 4. Strengthen Titles (MEDIUM PRIORITY)

## Current:

* Plain text labels

## Upgrade Options:

### Option A:

```text
Euclidean Space
──────────────
```

### Option B:

```text
Euclidean Space   [Flat Geometry]
Hyperbolic Space  [Curved Geometry]
```

---

## Goal:

Add meaning, not just labels

---

# 🎛️ 5. Reduce Sidebar Visual Weight (MEDIUM PRIORITY)

## Changes:

* Slightly darker background:

```css
background: #161616;
```

* Reduce button height
* Increase canvas contrast

---

## Goal:

Make canvas the primary focus

---

# ✨ 6. Replace Floating Tool Tooltip (HIGH PRIORITY)

## Current:

* Floating tooltip: “Active Tool: …”

## Replace with:

* Sidebar highlight for active tool
* Top status bar:

```text
Line Tool Active • Click two points
```

---

## Goal:

Cleaner, less intrusive UX

---

# 🎬 7. Add Motion & Feedback (MEDIUM PRIORITY)

## Required:

* Animated line drawing (progressive)
* Hover highlight on points
* Smooth transitions

---

## Goal:

Make system feel alive and interactive

---

# 🔥 8. Micro UI Polish (LOW COST, HIGH IMPACT)

## Add:

* Subtle divider between panels
* Improved typography (Inter / SF Pro)
* Increased padding in canvas

---

## Goal:

Refined, premium feel

---

# 🌟 OPTIONAL ENHANCEMENTS (FOR WOW FACTOR)

## Choose at least one:

### Option 1:

* Glow effect on geodesics

### Option 2:

* Animated grid fade-in

### Option 3:

* Cursor hover trail / highlight

---

# ⚠️ DESIGN CONSTRAINTS

* Do NOT overload UI with colors
* Do NOT reduce canvas size
* Do NOT add unnecessary shadows
* Maintain minimal aesthetic

---

# 🧪 SUCCESS CRITERIA

The UI should:

* Clearly differentiate both geometries visually
* Feel clean, modern, and intentional
* Keep user focus on the geometry
* Provide immediate spatial understanding

---

# 🏁 FINAL NOTE

The UI must communicate:

> Left = Flat space
> Right = Curved space

If this is not visually obvious, the design is incomplete.

