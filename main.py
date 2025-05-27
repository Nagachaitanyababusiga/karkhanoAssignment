import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt


class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.X, self.Y, self.Z = self._compute_coordinates()

    def _compute_coordinates(self):
        u = self.U
        v = self.V
        R = self.R

        X = (R + v * np.cos(u / 2)) * np.cos(u)
        Y = (R + v * np.cos(u / 2)) * np.sin(u)
        Z = v * np.sin(u / 2)

        return X, Y, Z

    def plot(self):
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, color='lightblue', edgecolor='gray', alpha=0.8)
        ax.set_title('Mobius Strip')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        plt.show()

    def surface_area(self):
        # Area element: || ∂r/∂u × ∂r/∂v ||
        du = self.u[1] - self.u[0]
        dv = self.v[1] - self.v[0]

        # Compute derivatives
        dX_du, dX_dv = np.gradient(self.X, du, dv, edge_order=2)
        dY_du, dY_dv = np.gradient(self.Y, du, dv, edge_order=2)
        dZ_du, dZ_dv = np.gradient(self.Z, du, dv, edge_order=2)

        # Cross product of partial derivatives
        cross_x = dY_du * dZ_dv - dZ_du * dY_dv
        cross_y = dZ_du * dX_dv - dX_du * dZ_dv
        cross_z = dX_du * dY_dv - dY_du * dX_dv

        area_density = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)

        # Integrate over the surface using Simpson’s rule
        area = simpson(simpson(area_density, self.v), self.u)
        return area

    def edge_length(self):
        # Boundary at v = -w/2 and v = w/2
        edges = []
        for boundary in [0, -1]:  # first and last rows
            x = self.X[boundary, :]
            y = self.Y[boundary, :]
            z = self.Z[boundary, :]
            coords = np.stack((x, y, z), axis=1)
            dists = np.linalg.norm(np.diff(coords, axis=0), axis=1)
            edges.append(np.sum(dists))

        return sum(edges)


if __name__ == "__main__":
    mobius = MobiusStrip(R=1.0, w=0.3, n=300)
    area = mobius.surface_area()
    edge = mobius.edge_length()

    print(f"Approximated Surface Area: {area:.4f}")
    print(f"Approximated Edge Length: {edge:.4f}")
    mobius.plot()

