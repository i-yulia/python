# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Неверно преобразует данные при восстановлении данных. Соединяет цифры в одно большое число.

def compression(d):
    count = 1
    res = ''
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            count += 1
        else:
            res = res + str(count) + d[i]
            count = 1
    if count > 1 or (d[len(d)-2] != d[-1]):
        res = res + str(count) + d[-1]
    return res

def recovery(d):
    number = ''
    res = ''
    for i in range(len(d)):
        if not d[i].isalpha(): # Возвращает флаг, указывающий на то, содержит ли строка только буквы.
            #Вернёт True , если в строке хотя бы один символ и все символы строки являются буквами, иначе — False .
            number += d[i]
        else:
            res = res + d[i] * int(number)
            number = ''
    return res

path = r'C:\Users\Юля\Desktop\Python\Seminars\HomeWork\HW\HWSeminar5\Task4(5)_input.txt'
data = open(path, 'r')
d = data.read().replace('\n', ' ')
res = recovery(compression(d))
print(f"Изначальный текст: {d}")
print(f"Текст после кодировки: {compression(d)}")
print(f"Текст после дешифровки: {res}")
data.close()

d2 = open('Task4(5)_recovery.txt', 'w')
d2.write(res)
d2.close()