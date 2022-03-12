# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python
# Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy

import random

numbers = [random.randrange(100) for x in range(10)]

print(numbers)

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)