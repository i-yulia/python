# 4. Реализуйте алгоритм перемешивания списка
from random import random

def list_mix(list_to_mix, mix_times):
    for i in range(0, mix_times):
        index1 = 0
        index2 = 0
        while index1 == index2:
            index1 = int(random() * len(list_to_mix))
            index2 = int(random() * len(list_to_mix))
        temp = list_to_mix[index1]
        list_to_mix[index1] = list_to_mix[index2]
        list_to_mix[index2] = temp
    return list_to_mix
listlen = int(input('Введите длину массива N: '))
my_list = []
for i in range(0,listlen):
    my_list.append(int(random() * listlen * 2 - listlen))
print(my_list)

mix_times = int(input("Введите количество перемешиваний списка: "))
print(list_mix(my_list, mix_times))