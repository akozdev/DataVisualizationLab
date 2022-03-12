# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.


def isRectTriangle(a, b, c):
    if (a+b>c) or (a+c>b) or (b+c>a):
        print('Cannot create such triangle')
        return False

    sum = pow(a, 2) + pow(b, 2)

    return True if sum == pow(c, 2) else False


print(isRectTriangle(3, 4, 5))
print(isRectTriangle(3, 4, 24))
