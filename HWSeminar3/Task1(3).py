#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

list_len = int(input("Введите длину списка: "))
my_list = []
for i in range(list_len):

    new_n = random.randrange(0, 20)
    my_list.append(new_n)
print(f"Ваш список: {my_list}")
sum_el = 0
for i in range(1, len(my_list), 2):
    sum_el += int(my_list[i])
print(f"Сумма элементов на нечетных позициях: {sum_el}")