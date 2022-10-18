#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
import random


def prod_el(num_list):
    even_len = 0
    new_list = []
    if not len(num_list) % 2 == 0:
        even_len = int((len(num_list) + 1) / 2)
    else:
        even_len = int(len(num_list) / 2)
    for i in range(0, even_len):
        new_list.append(num_list[i] * (num_list[len(num_list) - i - 1]))
    return new_list

num_user = int(input("Введите длину списка: "))
my_list = []
for i in range(num_user):
    new_n = random.randrange(0, 10)
    my_list.append(new_n)
print(f"Ваш список: {my_list}")
mult_list = prod_el(my_list)
print(f'{my_list} => {mult_list}')
