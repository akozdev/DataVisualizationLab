# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile
# elementów ma mnożyć)

import functools


def calcProductOfSeries(a=1, b=4, howMany=10):
    series = [x * b for x in range(a, a + howMany)]
    return functools.reduce(lambda a, b: a * b, series)


print(calcProductOfSeries(1, 2, 2))
print(calcProductOfSeries())
