# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.

import functools


def calcProductOfSeries(a=1, b=4, howMany=10):
    series = [x * b for x in range(a, a + howMany)]
    return functools.reduce(lambda a, b: a * b, series)


print(calcProductOfSeries(1, 2, 2))
print(calcProductOfSeries())