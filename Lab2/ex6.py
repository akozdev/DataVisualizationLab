# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od
# wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.

try:
    a = int(input('Input number a: '))
    b = int(input('Input number b: '))
    c = int(input('Input number c: '))

    numbers = [a, b, c]

    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    print(f'Max number is {max_num}')

except ValueError:
    print('Number must be an integer')
