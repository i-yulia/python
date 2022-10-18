#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число N: "))
divider = 2
list_div = []
while n >= divider:
    if n % divider == 0:
        list_div.append(divider)
        n /= divider
    else:
        divider +=1
print((list_div))
