# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a
# wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do
# zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.

products = {
    'jajko': 'sztuka',
    'mleko': 'litr',
    'chleb': 'sztuka',
    'ziemniaki': 'kg'
}

new_products = {value: key for key, value in products.items()}

print(new_products)
