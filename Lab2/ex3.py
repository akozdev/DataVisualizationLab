# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co
# wartością w takim słowniku. Policz liczbę elementów w słowniku.

fav_computer_games = {
    'Minecraft': {
        'studio': 'Mojang Studios',
        'released': '2011-11-18'
    },
    'Terraria': {
        'studio': 'Re-Logic',
        'released': '2011-05-16'
    }
}

fav_computer_games_count = len(fav_computer_games)

print(fav_computer_games)
print(fav_computer_games_count)  # 2
