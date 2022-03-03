# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write())

f = open('./ex4_input.txt')
numbers = f.readlines()
f.close()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

result = pow(a, b) + c

output_file = open('./ex4_output.txt', 'w')
output_file.write(f'The result of {a}^{b} + {c} is {result}')
output_file.close()
