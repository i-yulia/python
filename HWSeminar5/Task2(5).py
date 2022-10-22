#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
from random import randint

count_of_candies = 2021
player1 = "1"
player2 = "2"
current_player = (randint(1, 2))
print(f"Первым ходит игрок под номером: {current_player}")

while count_of_candies > 0:
    print(f'количество оставшихся конфет: {count_of_candies}')
    while True:
        number_to_delete = int(input(f'ход игрока {current_player} (1 - 28): '))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
    count_of_candies -= number_to_delete
    current_player = player1 if current_player == player2 else player2
current_player = player1 if current_player == player2 else player2
print(f'Победил игрок под №: {current_player}')