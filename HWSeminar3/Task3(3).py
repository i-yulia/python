# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

num_leng = int(input("Введите длину списка: "))
my_list = []
num_n = 0
for i in range(num_leng):
    num_n = round(random.uniform(0, 10), 2)
    my_list.append(num_n)
print(f"Ваш список: {my_list}")
max_num = my_list[0] % 1
min_num = my_list[0] % 1
new_list = [num % 1 for num in my_list]
print(round(max(new_list), 2))
print(round(min(new_list), 2))
print(round(max(new_list) - min(new_list), 2))



