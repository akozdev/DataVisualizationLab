# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne

import math

# String
string_a = 'Hello'
string_b = 'Hi'

print(string_a, string_b)

# Integer
integer_a = 5
integer_b = 10

print(integer_a, integer_b)

# Float
float_a = 1.5
float_b = 10.3

print(float_a, float_b)

# Boolean
boolean_a = True
boolean_b = False

print(boolean_a, boolean_b)

# Complex
complex_a = 1 + 2j
complex_b = math.sqrt(3) - 5j

print(complex_a, complex_b)

# List
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

print(list_a, list_b)

# Dictionary
dict_a = {'id': 0, 'firstName': 'John', 'lastName': 'Doe'}
dict_b = {'path': '/', 'method': 'GET'}

print(dict_a, dict_b)

# Set
set_a = {'apple', 'banana', 'berry'}
set_b = {'Earth', 'Mercury', 'Venus'}

print(set_a, set_b)

# Frozen set
frozen_set_a = frozenset(('a', 'b', 'c', 'd'))
frozen_set_b = frozenset(('Earth', 'Mercury', 'Venus'))

print(frozen_set_a, frozen_set_b)

# Tuple
tuple_a = ('apple', 'banana', 'berry')
tuple_b = ('Earth', 'Mercury', 'Venus')

print(tuple_a, tuple_b)

# Range
range_a = range(1, 11)
range_b = range(0, 99)

print(range_a, range_b)

# Bytes
bytes_a = bytes('Hello, World!', 'utf-8')
bytes_b = bytes('This string will be converted to immutable bytes object', 'utf-8')

print(bytes_a, bytes_b)

# Byte array
bytes_array_a = bytearray([1, 2, 3, 4, 5])
bytes_array_b = bytearray('This string will be converted to mutable bytes object', 'utf-8')

print(bytes_array_a, bytes_array_b)
