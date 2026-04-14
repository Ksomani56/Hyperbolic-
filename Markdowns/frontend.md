# Dual Geometry Visualizer - Web App Architecture & Design Plan

## 1. Executive Summary
Transitioning the Python/Pygame visualizer into a sleek, interactive React + Next.js web application. This frontend will feature a professional, minimal aesthetic (Linear-style design) avoiding neon/cliché "AI" color palettes. The focus is on crisp typography, high-contrast monochrome layouts, and seamless canvas interactions.

## 2. Tech Stack
* **Framework:** Next.js (App Router)
* **UI Library:** React 18
* **Styling:** Tailwind CSS (configured for a strict minimal grayscale palette)
* **Icons:** Lucide React (clean, minimal line icons)
* **State Management:** Zustand (for lightweight, global geometry state & playback sync)
* **Rendering Engine:** HTML5 Canvas Api through Custom React Hooks (for high-FPS geodesic and arc rendering).

## 3. Design System: Professional Minimalism
We are avoiding vibrant purples, glows, and "gamer" aesthetics. The vibe is a rigorous academic laboratory or a high-end enterprise design tool.

### Color Palette (Slate & Zinc Focus)
* **Background:** `--bg-base` `#fafafa` (Light) / `#09090b` (Dark)
* **Panels/Sidebar:** `--bg-panel` `#ffffff` (Light) / `#18181b` (Dark)
* **Borders:** `--border` `#e4e4e7` (Light) / `#27272a` (Dark)
* **Primary Text:** `--text-primary` `#18181b` (Light) / `#fafafa` (Dark)
* **Secondary Text:** `--text-muted` `#a1a1aa` (Light) / `#a1a1aa` (Dark)
* **Euclidean Accent:** `--accent-euc` `#3b82f6` (Clean Blue, subdued)
* **Hyperbolic Accent:** `--accent-hyp` `#f97316` (Terracotta Orange, subdued)
* **Highlight:** `--accent-active` `#18181b` (Dark mode: `#ffffff`) indicating active tools.

### Typography
* **Primary Font:** Inter or Geist (sans-serif) for high legibility in UI.
* **Serif/Math Font:** Computer Modern or mathematical serif for tooltips and theorems to maintain an academic feel.

## 4. Layout Architecture
A 3-pane layout utilizing strict CSS Grid.

```text
 -----------------------------------------------------
| Sidebar  | Euclidean Plane      | Hyperbolic Disk    |
| (280px)  | (Flexible Width)     | (Flexible Width)   |
| - Tools  |                      |                    |
| - Demos  |      <Canvas />      |     <Canvas />     |
| - Action |                      |                    |
 -----------------------------------------------------
```

### Components
1. **`Sidebar`**: Left fixed panel container.
   - **`ToolGroup`**: Radio-button style toggles for Point, Line, Triangle, Distance, Parallel.
   - **`DemoPresets`**: Buttons triggering predefined state injections.
   - **`PlaybackControls`**: Minimalist media controls (Play/Pause/Scrub).
2. **`Workspace`**: The main split-view container.
   - **`CanvasOverlay`**: A React layer for floating tooltips.
   - **`EuclideanCanvas`**: Renders straight lines and flat space measurements.
   - **`HyperbolicCanvas`**: Renders Poincaré disk, geodesics, boundary circle, and defect calculations.

## 5. State Management & Sync
All logic currently handled by `core.engine` (in Python) will be ported to a Zustand store.

```javascript
// store.js
import { create } from 'zustand'

export const useGeometryStore = create((set) => ({
  points: {},
  lines: {},
  triangles: {},
  currentTool: 'point',
  explainMode: false,
  
  // Actions
  addPoint: (x, y) => set((state) => { ... }),
  addLine: (p1, p2) => set((state) => { ... }),
  undo: () => set((state) => { ... }),
  loadPreset: (type) => set((state) => { ... }),
}))
```

## 6. Rendering Strategy
* We will use a `useCanvas` hook:
  * A single `<canvas>` element per workspace.
  * A perfectly functional `draw(ctx, state)` method that hits exactly 60 FPS natively.
  * The heavily mathematical logic (`hyperbolic_distance`, circle inversion) from Python will be translated into pure TypeScript functions.

## 7. Interactive Polish
* **Snap to Grid:** Invisible snap targets when hovering on intersections in Euclidean space.
* **Hover Effects:** Minimal box shadows and soft transition timings (150ms ease-in-out) on UI elements.
* **Dark Mode:** A native toggle at the bottom of the sidebar.
