# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


def accuracy(number):
    result = 0
    while number % 1 > 0:
        number *= 10
        result += 1
    return result


number = float(input("Введите точность: "))
rounded_pi = round(math.pi, accuracy(number))
print(rounded_pi)