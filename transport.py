import numpy as np


def transportation_nw(cost, supply, demand):
    cost = np.array(cost, dtype=float)
    supply = np.array(supply, dtype=float)
    demand = np.array(demand, dtype=float)

    m, n = cost.shape
    X = np.zeros((m, n))

    i = 0
    j = 0
    while i < m and j < n:
        q = min(supply[i], demand[j])
        X[i, j] = q
        supply[i] -= q
        demand[j] -= q
        if supply[i] <= 1e-9:
            i += 1
        if demand[j] <= 1e-9:
            j += 1

    total_cost = float((X * cost).sum())
    return X, total_cost


#example:
cost = [
    [2, 3, 1],
    [5, 4, 8],
    [5, 6, 8]
]
supply = [20, 30, 25]
demand = [10, 35, 30]

X, z = transportation_nw(cost, supply, demand)
print("Plan:")
print(X)
print("Total cost:", z)
