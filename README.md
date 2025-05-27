# Möbius Strip 3D Model and Geometry Calculator

This Python project models a Möbius strip using parametric equations and calculates key geometric properties including surface area and edge length. It also includes 3D visualization of the strip.

---

## 🧠 Description

The Möbius strip is a non-orientable surface with only one side and one boundary. This project:
- Uses parametric equations to construct a 3D mesh of the strip.
- Approximates its surface area using Simpson's rule.
- Computes the boundary (edge) length numerically.
- Provides a 3D visualization using Matplotlib.

---

## 🧮 Parametric Equations

The strip is defined using the following parametric equations:

x(u, v) = (R + v * cos(u / 2)) * cos(u)
y(u, v) = (R + v * cos(u / 2)) * sin(u)
z(u, v) = v * sin(u / 2)


Where:
- `u ∈ [0, 2π]` (angle around the central circle)
- `v ∈ [-w/2, w/2]` (width of the strip)

---

## 🧾 Features

- ✅ Modular `MobiusStrip` class with configurable parameters
- ✅ Numerical integration using Simpson's Rule
- ✅ 3D visualization using `matplotlib`
- ✅ Calculates:
  - Surface area of the strip
  - Length of the boundary (single edge)

---

## 📦 Dependencies

Make sure you have the following Python packages installed:

```bash
pip install numpy matplotlib scipy
```

✍️ Author
S.NagaChaitanyababu
📧 [nagachaitanyababusiga@gmail.com]
