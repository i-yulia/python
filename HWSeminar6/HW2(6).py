# Задача 1 из д/з к семинару 2.
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
s = 0
users_num = input('Укажите вещественное число: ')
res = list(map(int, [num for num in users_num if num.isdigit()]))
for el in res:
    s += el
print(s)

