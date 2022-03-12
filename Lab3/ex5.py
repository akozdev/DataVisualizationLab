# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.

def calcTrapezoidField(a=1, b=1, h=2):
    field = ((a + b) * h) / 2
    return field


print(calcTrapezoidField(9, 3, 3))
