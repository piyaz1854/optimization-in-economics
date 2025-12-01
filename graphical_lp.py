import numpy as np
import math
import matplotlib.pyplot as plt


def graphical_lp(A, b, c, sense="max"):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    m = A.shape[0]
    lines = [tuple(A[i]) + (b[i],) for i in range(m)]
    lines.append((1.0, 0.0, 0.0))
    lines.append((0.0, 1.0, 0.0))

    pts = []

    for i in range(len(lines)):
        a1, a2, b1 = lines[i]
        for j in range(i + 1, len(lines)):
            c1, c2, b2 = lines[j]

            det = a1 * c2 - a2 * c1
            if abs(det) < 1e-9:
                continue

            x = (b1 * c2 - b2 * a2) / det
            y = (a1 * b2 - c1 * b1) / det

            if x < -1e-9 or y < -1e-9:
                continue

            if np.all(A.dot(np.array([x, y])) <= b + 1e-9):
                pts.append((x, y))

    uniq = []
    for p in pts:
        if not any(abs(p[0] - q[0]) < 1e-6 and abs(p[1] - q[1]) < 1e-6 for q in uniq):
            uniq.append(p)
    pts = uniq

    if not pts:
        print("No feasible region")
        return None

    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    pts_sorted = sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

    zs = [c.dot(np.array(p)) for p in pts_sorted]
    if sense == "max":
        best_idx = int(np.argmax(zs))
    else:
        best_idx = int(np.argmin(zs))

    best_pt = pts_sorted[best_idx]
    best_z = zs[best_idx]

    return pts_sorted, zs, best_pt, best_z


def plot_graphical_lp(A, b, c, sense="max"):
    result = graphical_lp(A, b, c, sense=sense)
    if result is None:
        return
    pts, zs, best_pt, best_z = result

    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]

    plt.figure()
    plt.fill(xs, ys, alpha=0.25)
    plt.scatter([best_pt[0]], [best_pt[1]], marker='*', s=200)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"{sense}: ({best_pt[0]:.2f}, {best_pt[1]:.2f}), z={best_z:.2f}")
    plt.show()


#example:
A = [
    [1, 1],
    [1, 0],
    [0, 1]
]
b = [4, 2.5, 3]
c = [3, 5]

pts, zs, best_pt, best_z = graphical_lp(A, b, c, sense="max")
plot_graphical_lp(A, b, c, sense="max")

pts_min, zs_min, best_pt_min, best_z_min = graphical_lp(A, b, c, sense="min")
plot_graphical_lp(A, b, c, sense="min")
