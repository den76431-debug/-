list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# Колво игроков в списке
total_players = len(list_players)

# Середина списка
mid = total_players // 2

# Первая команда
team1 = list_players[:mid]

# Вторая команда
team2 = list_players[mid:]

# вывод
print(team1)
print(team2)


