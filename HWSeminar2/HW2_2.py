# №2. Напишите программу, которая принимает на вход число num и выдает набор произведений чисел от 1 до num.

# Пример:

# - пусть num = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
num = int(input("Введите целое число: "))
num_product = 1
result_num_product = []
for i in range(1, num + 1):
    num_product *= i
    result_num_product.append(num_product)  # append добавляет в список числа из списка
print(f"{result_num_product} ")
