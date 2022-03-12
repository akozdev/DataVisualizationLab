# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}


A = [1-x for x in range(1, 11)]

print(A)  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

B = [pow(4, x) for x in range(0, 8)]

print(B)

C = [x for x in B if x % 2 == 0]

print(C)