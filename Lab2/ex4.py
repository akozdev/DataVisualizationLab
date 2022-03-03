# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji
# input

user_input = input('Input some text: ')

count_of_a = user_input.count('a')

print(f"Your input contains {count_of_a} occurrences of the 'a' letter")
