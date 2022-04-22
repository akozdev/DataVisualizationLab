import numpy as np


def create_diag(v_length):
    v = np.flip(np.arange(1, v_length + 1))
    return np.diag(v)


print(create_diag(5))

'''
[[5 0 0 0 0]
 [0 4 0 0 0]
 [0 0 3 0 0]
 [0 0 0 2 0]
 [0 0 0 0 1]]
'''