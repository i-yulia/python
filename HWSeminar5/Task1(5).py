# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_str = str("вба абв123 абв456абв789 все !")
my_list = my_str.split(" ")
result = []
for word in my_list:
    if "абв" not in word:
        result.append(word)
print(" ".join(result))
