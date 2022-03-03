# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą
# użycia pętli for podnieś każdą liczbę do kwadratu.

numbers = [1, 2, 3.5, 4.6, 7]
numbers_squared = []

for num in numbers:
    numbers_squared.append(pow(num, 2))

print(numbers_squared)  # [1, 4, 12.25, 21.159999999999997, 49]