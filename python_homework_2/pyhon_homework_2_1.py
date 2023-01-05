# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

float_num = input('Input number: ')
sum_of_digits = 0
for i in float_num:
    if i.isdigit():
        sum_of_digits += int(i)

print(sum_of_digits)
