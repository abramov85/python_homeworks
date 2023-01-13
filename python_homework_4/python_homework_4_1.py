# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def create_polynom(max_degree, min_k, max_k):
    my_dict = {max_degree: 0}
    while my_dict[max_degree] == 0:
        my_dict = {max_degree: random.randint(-100, 100)}
    equation = f'{my_dict[max_degree]}*x**{max_degree} '
    for i in range(max_degree - 1, -1, -1):
        if random.randint(0, 3) != 0:  # добавить побольше нулевых коэффициентов
            my_dict[i] = random.randint(min_k, max_k)
        else:
            my_dict[i] = 0
        if my_dict[i] != 0:
            equation += f'+ {my_dict[i]}*x**{i} '
    equation = equation.replace('**1 ', ' ')\
        .replace('*x**0', '')\
        .replace(' 1*x', ' x')\
        .replace(' + -', ' - ')\
        .replace('-1*', '-')
    if equation.startswith('1*'):
        equation = equation.replace('1*', '')
    equation += '= 0'
    return equation, my_dict


k = int(input('Введите максимальную степень многочлена: '))
polynom, koef = create_polynom(k, -100, 100)
print(polynom)
print(koef)

with open('task1.txt', 'w', encoding='UTF-8') as data:
    data.write(polynom)

polynom_1_for_task_2 = create_polynom(8, -100, 100)[0]
polynom_2_for_task_2 = create_polynom(11, -100, 100)[0]
with open('polynom1.txt', 'w', encoding='UTF-8') as data:
    data.write(polynom_1_for_task_2)
with open('polynom2.txt', 'w', encoding='UTF-8') as data:
    data.write(polynom_2_for_task_2)


