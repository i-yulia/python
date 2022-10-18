# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
k = int(input('Введите число: '))
fib = []
temp = 0
count = 0
for i in range(0, k + 1):
    fib.append(temp)
    if temp == 0:
        temp = 1
    temp += fib[i - 1]
negativ_list = []
count = len(fib) - 1
for i in range(len(fib)):
    if fib[i] != 0 and i % 2 == 0:
        negativ_list.append(fib[i] * -1)
    elif i % 2 != 0:
        negativ_list.append(fib[i])
negativ_list = negativ_list[::-1]
negativ_list.extend(fib)

print(negativ_list)



