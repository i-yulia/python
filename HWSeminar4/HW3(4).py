#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


def find_unique_numbers(your_list):
    unique_list =[]
    for num in your_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


str_num = str(input("Введите числа через пробел: "))
list_num = [int(x) for x in str_num.split()]
result = find_unique_numbers(list_num)
print(result)
print(list(set(list_num)))
