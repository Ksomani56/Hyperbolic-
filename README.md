# Dual Geometry Visualizer: Euclidean vs Non-Euclidean

An interactive educational platform designed to visually demonstrate the differences between Euclidean and Hyperbolic geometry using a real-time, split-screen interface.

## 🧠 Core Concept

> **Same input → different geometry → different results**

The visualizer provides a dual canvas:
- **Left Panel:** Euclidean Plane
- **Right Panel:** Hyperbolic Space (Poincaré Disk Model)

Actions drawn in standard Euclidean space are continuously synchronized and mapped onto the hyperbolic space, dynamically translating straight lines into geodesics (circular arcs orthogonal to the unit disk's boundary) and clearly displaying non-Euclidean geometric properties.

---

## ✨ Features

- **Split-Screen Visualization:** Simultaneously interact with the Cartesian grid and the Poincaré Unit Disk.
- **Real-Time Geodesic Rendering:** Maps Euclidean objects seamlessly into hyperbolic space.
- **Interactive Tools:** Point and Line drawing tools designed to demonstrate mathematical principles.
- **Educational Demonstrations:**
  - *Triangle Angle Sum:* Demonstrates how a triangle's interior angles sum to 180° in Euclidean space, but strictly less than 180° (and relative to area) in Hyperbolic space.
- **Playback System:** Record user actions to be replayed sequentially as a demonstration.

---

## 🏗️ Architecture

The project contains both a Python desktop engine and a web-based interface structure:

- `core/` & `geometry/` - The unified math and engine logic underlying the syncing and object transformations.
- `ui/` - Python/Pygame-based rendering pipelines.
- `web/` - A modern React/Next.js frontend implementation of the visualizer.
- `Markdowns/` - Contains exhaustive product specs, design documents, and theoretical references.

---

## 🚀 Getting Started

### Python Desktop App Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ksomani56/Hyperbolic-.git
   cd Hyperbolic-
   ```

2. **Install dependencies:**
   Make sure you have Python 3.x installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the visualizer:**
   ```bash
   python main.py
   ```

### Web Interface Setup

1. Navigate to the `web` directory:
   ```bash
   cd web
   ```
2. Install frontend dependencies and run the development server:
   ```bash
   npm install
   npm run dev
   ```

---

## 📚 Educational Value

This visualizer is specifically tailored for:
- **Engineering and Math Students** looking for direct visual feedback of non-Euclidean axioms.
- **Professors** serving as a hands-on teaching tool in lectures.
- **Hackathons** presenting robust, math-engine-driven visualization paradigms.

Built with performance and clarity in mind, it prioritizes intuitive user experience to make complex hyperbolic geometry principles readily accessible.
