# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko
# parzyste liczby.

even_numbers = []

try:
    count = 1
    while count <= 10:
        number = int(input('Input an integer: '))
        if number % 2 == 0:
            even_numbers.append(number)
        count += 1
except ValueError:
    print('Input must be an integer')

print(even_numbers)
