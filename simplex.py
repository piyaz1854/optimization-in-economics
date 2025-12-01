import numpy as np


def simplex(A, b, c, sense="max"):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    if sense == "min":
        c = -c

    m, n = A.shape

    T = np.zeros((m + 1, n + m + 1))
    T[:m, :n] = A
    T[:m, n:n + m] = np.eye(m)
    T[:m, -1] = b
    T[-1, :n] = -c

    basis = list(range(n, n + m))

    while True:
        col = np.argmin(T[-1, :-1])
        if T[-1, col] >= -1e-9:
            break

        ratios = []
        for i in range(m):
            if T[i, col] > 1e-9:
                ratios.append(T[i, -1] / T[i, col])
            else:
                ratios.append(np.inf)

        row = int(np.argmin(ratios))
        if not np.isfinite(ratios[row]):
            return None, np.inf, "unbounded"

        pivot = T[row, col]
        T[row, :] /= pivot
        for i in range(m + 1):
            if i != row:
                T[i, :] -= T[i, col] * T[row, :]

        basis[row] = col

    x = np.zeros(n)
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = T[i, -1]

    z = T[-1, -1]
    if sense == "min":
        z = -z

    return x, z, "optimal"


A = [
    [1, 1],
    [1, 0],
    [0, 1]
]
b = [4, 2.5, 3]
c = [3, 5]

x_max, z_max, status_max = simplex(A, b, c, sense="max")
print("max:", status_max, "x* =", x_max, "z* =", z_max)

x_min, z_min, status_min = simplex(A, b, c, sense="min")
print("min:", status_min, "x* =", x_min, "z* =", z_min)
