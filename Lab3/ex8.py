# Zad8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz
# to nazwa produktu a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i
# zwracać całościową wartość tych produktów.

import functools


shopping_list = {
    'mleko': 3,
    'ziemniaki': 2,
    'ser': 8,
    'makaron': 4,
    'ketchup': 3
}


def calc_total_cost(shopping_list):
    count_of_items = len(shopping_list)
    print(count_of_items)
    total_price = functools.reduce(lambda a,b: a+b, shopping_list.values())
    print(total_price)

    return [count_of_items, total_price]



print(calc_total_cost(shopping_list))