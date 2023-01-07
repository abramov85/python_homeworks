# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
my_list = [2, 3, 5, 9, 3, 4, 1, 7]
sum_odd = 0

for i in range(1, len(my_list), 2):
    sum_odd += my_list[i]


def odd_elements(new_list):
    elements = str()
    for item in range(1, len(new_list), 2):
        if item == 1:
            elements += str(new_list[item])
        else:
            elements += ' и ' + str(new_list[item])
    return elements


print(f'{my_list} -> на нечётных позициях элементы {odd_elements(my_list)}, ответ: {sum_odd} ')
