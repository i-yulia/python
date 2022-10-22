#Игра с конфетами против бота

import random
from random import randint

count_of_candies = 2021
player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
print(f"Имя второго игрока: {player2}")
players = [player1, player2]
current_player = random.choice(players)
print(f"Первым ходит: {current_player}")
while count_of_candies > 0:
    if current_player == player1:
        print(f"Количество оставшихся конфет: {count_of_candies}")
        number_to_delete = int(input(f"ход игрока: {player1} (1 - 28): "))
        if number_to_delete > 28 or number_to_delete < 1 or number_to_delete > count_of_candies:
            print("Некорректный ввод. Введите число от 1 до 28. Обратите внимание, число не должно превышать количества оставшихся конфет")
            continue
        count_of_candies -= number_to_delete
        if count_of_candies == 0:
            break
        current_player = player2
    if current_player == player2:
        print(f"количество оставшихся конфет: {count_of_candies}")
        number_to_delete = (randint(1, 28))
        print(f"Ход игрока Bot: {number_to_delete}")
        if number_to_delete > count_of_candies:
            print("Число не должно превышать количества оставшихся конфет. Введите число: ")
            continue
        else:
            count_of_candies -= number_to_delete
            if count_of_candies == 0:
                break
            current_player = player1
print(f"Победил игрок под именем: {current_player}")
