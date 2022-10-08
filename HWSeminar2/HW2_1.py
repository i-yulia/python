# №1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

num = float (input("Введите число: "))
num_str = str(num)
sum_num = 0
for i in num_str:
    if i != '.' and i != '-':
        sum_num += int(i)
print(sum_num)


