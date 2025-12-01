# Economic Linear Programming Models in Python

This repository contains simple Python implementations of classical mathematical modelling methods used in economics:

- Graphical solution of a 2D linear programming problem
- Simplex method (max & min)
- Transportation problem (North-West corner method)
- Assignment problem (brute force for small sizes)

All code is minimalistic and focused on educational use in class.

---

## Installation

Create and activate a virtual environment (optional but recommended), then install dependencies:

```
pip install -r requirements.txt
Typical requirements.txt:
contourpy==1.3.3
cycler==0.12.1
fonttools==4.61.0
kiwisolver==1.4.9
matplotlib==3.10.7
numpy==2.3.5
packaging==25.0
pillow==12.0.0
pyparsing==3.2.5
python-dateutil==2.9.0.post0
six==1.17.0
```
## 1. Graphical solution of LP
Solves a 2D linear programming problem of the form
maximize or minimize
z = c1 * x + c2 * y
subject to A [x, y]^T <= b, x >= 0, y >= 0
and draws the feasible region and the optimal point.
Example:
```
from lp_graphical import graphical_lp, plot_graphical_lp

A = [
    [1, 1],
    [1, 0],
    [0, 1]
]
b = [4, 2.5, 3]
c = [3, 5]

pts, zs, best_pt, best_z = graphical_lp(A, b, c, sense="max")

print("Vertices:")
for (x, y), z in zip(pts, zs):
    print(f"({x:.2f}, {y:.2f}) -> z = {z:.2f}")

print("\nOptimal solution:")
print("x* =", best_pt[0])
print("y* =", best_pt[1])
print("z* =", best_z)

plot_graphical_lp(A, b, c, sense="max")
```
# 2. Simplex method
Solves linear programming problems in standard form
maximize or minimize
c^T * x
subject to A * x <= b, x >= 0
using a basic simplex tableau implementation.
Example:
```
from lp_simplex import simplex

A = [
    [1, 1],
    [1, 0],
    [0, 1]
]
b = [4, 2.5, 3]
c = [3, 5]

x_max, z_max, status_max = simplex(A, b, c, sense="max")
print("Maximization:")
print("status:", status_max)
print("x*:", x_max)
print("z*:", z_max)

x_min, z_min, status_min = simplex(A, b, c, sense="min")
print("\nMinimization:")
print("status:", status_min)
print("x*:", x_min)
print("z*:", z_min)
```
# 3. Transportation problem
Balanced transportation problem with supplies, demands and a cost matrix.
The implementation uses the North-West corner method to construct a feasible plan.
Example:
```
from transport import transportation_nw
import numpy as np

cost = [
    [2, 3, 1],
    [5, 4, 8],
    [5, 6, 8]
]
supply = [20, 30, 25]
demand = [10, 35, 30]

X, z = transportation_nw(cost, supply, demand)
print("Transportation plan:")
print(np.array(X))
print("Total cost:", z)
```
4. Assignment problem
Assignment problem for a square cost matrix, solved by brute force.
Suitable for small sizes (3x3, 4x4, 5x5) in teaching examples.
Example:
```
from assignment import assignment_bruteforce

cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

perm, z = assignment_bruteforce(cost)
print("Best assignment (worker i -> task perm[i]):")
print(perm)
print("Total cost:", z)
```