import numpy as np


def create_nd_array(n):
    return np.arange(1, n*n+1).reshape(n, n)


print(create_nd_array(5))

'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
'''