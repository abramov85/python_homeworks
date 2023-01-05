# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Input count of numbers: '))
my_list = []
my_sum = 0

for i in range(n):
    my_list.append(round((1 + 1/(i+1))**(i+1), 2))
    my_sum += round((1 + 1/(i+1))**(i+1), 2)

print(my_list)
print(my_sum)
