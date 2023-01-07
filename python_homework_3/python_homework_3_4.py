# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Input integer number: '))
num_str = str()

while num > 0:
    num_str += str(num % 2)
    num = num//2

for i in range(len(num_str)):
    num += int(num_str[i])*2**i

num_str = num_str[::-1]

print(f'{num} -> {num_str}')
