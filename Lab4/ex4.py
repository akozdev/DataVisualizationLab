import numpy as np


def create_logspace(base, q):
    return np.logspace(1, q, num=q, dtype=int, base=base)


print(create_logspace(2, 4))  # [2 4 8 16]
print(create_logspace(3, 5))  # [3 9 27 81 243]
