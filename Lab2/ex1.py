# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej
# lubiane sporty na sam koniec.

sport_disciplines = ['Fencing', 'Football', 'Skiing']

sport_disciplines_reversed = []

for sport in reversed(sport_disciplines):
    sport_disciplines_reversed.append(sport)

sport_disciplines_reversed.append('Swimming')

print(sport_disciplines_reversed)
