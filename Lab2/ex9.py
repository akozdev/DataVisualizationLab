# Zad. 9.
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda
# wartość ujemną to powinien być wyłapany błąd.

import math

try:
    number = float(input('Input a positive number: '))
    result = math.sqrt(number)
    print(result)
except ValueError:
    print('The input has to be a positive number')
