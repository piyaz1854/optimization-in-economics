import numpy as np
import itertools


def assignment_bruteforce(cost):
    cost = np.array(cost, dtype=float)
    n, m = cost.shape
    assert n == m
    best_perm = None
    best_cost = float("inf")

    for perm in itertools.permutations(range(n)):
        c = 0.0
        for i in range(n):
            c += cost[i, perm[i]]
        if c < best_cost:
            best_cost = c
            best_perm = perm

    return best_perm, best_cost



#example:
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
