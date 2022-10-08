# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}
num = int(input('Введите число: '))
my_list = {}
result_sum = 0
for key in range(1, num + 1):
    my_list[key] = round((1 + 1 / key) ** key, 2)
    result_sum += my_list[key]
print(f'{num}: {my_list} \nсумма = {round(result_sum, 3)}')
