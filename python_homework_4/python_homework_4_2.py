# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
with open('polynom1.txt', 'r', encoding='UTF-8') as data:
    polynom_1 = data.read()

with open('polynom2.txt', 'r', encoding='UTF-8') as data:
    polynom_2 = data.read()

polynom_1 = polynom_1.replace('- ', '+-')\
    .replace(' ', '')\
    .replace('=0', '')\
    .replace('x**', ':')\
    .replace('*', '')\
    .replace('x', ':1')
polynom_2 = polynom_2.replace('- ', '+-')\
    .replace(' ', '')\
    .replace('=0', '')\
    .replace('x**', ':')\
    .replace('*', '')\
    .replace('x', ':1')

polynom_1_list = polynom_1.split('+')
polynom_2_list = polynom_2.split('+')

if ':' not in polynom_1_list[-1]:
    polynom_1_list[-1] += ':0'
if ':' not in polynom_2_list[-1]:
    polynom_2_list[-1] += ':0'

polynom_1_dict = {}
polynom_2_dict = {}

for i in range(len(polynom_1_list)):
    polynom_1_dict[int(polynom_1_list[i].split(':')[1])] = int(polynom_1_list[i].split(':')[0])

for i in range(len(polynom_2_list)):
    polynom_2_dict[int(polynom_2_list[i].split(':')[1])] = int(polynom_2_list[i].split(':')[0])

max_degree = max(max(polynom_1_dict.keys()), max(polynom_2_dict.keys()))

polynom_sum_dict = {}
polynom_sum = str()

for i in range(max_degree, -1, -1):
    polynom_sum_dict[i] = polynom_1_dict.get(i, 0) + polynom_2_dict.get(i, 0)
    if i == max_degree:
        if polynom_sum_dict[i] == 1:
            polynom_sum += f'x**{i} '
        elif polynom_sum_dict[i] == -1:
            polynom_sum += f'-x**{i} '
        elif polynom_sum_dict[i] < -1:
            polynom_sum += f'-{polynom_sum_dict[i] * -1}*x**{i} '
        elif polynom_sum_dict[i] > -1:
            polynom_sum += f'{polynom_sum_dict[i]}*x**{i} '
    elif max_degree > i > 1:
        if polynom_sum_dict[i] == 1:
            polynom_sum += f'+ x**{i} '
        elif polynom_sum_dict[i] == -1:
            polynom_sum += f'- x**{i} '
        elif polynom_sum_dict[i] < -1:
            polynom_sum += f'- {polynom_sum_dict[i] * -1}*x**{i} '
        elif polynom_sum_dict[i] > 1:
            polynom_sum += f'+ {polynom_sum_dict[i]}*x**{i} '
    elif i == 1:
        if polynom_sum_dict[i] == 1:
            polynom_sum += f'+ x '
        elif polynom_sum_dict[i] == -1:
            polynom_sum += f'- x '
        elif polynom_sum_dict[i] < -1:
            polynom_sum += f'- {polynom_sum_dict[i] * -1}*x '
        elif polynom_sum_dict[i] > -1:
            polynom_sum += f'+ {polynom_sum_dict[i]}*x '
    elif i == 0:
        if polynom_sum_dict[i] == 1:
            polynom_sum += f'+ 1 = 0'
        elif polynom_sum_dict[i] == -1:
            polynom_sum += f'- 1 = 0 '
        elif polynom_sum_dict[i] < -1:
            polynom_sum += f'- {polynom_sum_dict[i] * -1} = 0'
        elif polynom_sum_dict[i] > -1:
            polynom_sum += f'+ {polynom_sum_dict[i]} = 0'

with open('polynom_sum.txt', 'w', encoding='UTF-8') as data:
    data.write(polynom_sum)

print(polynom_1_dict)
print(polynom_2_dict)
print(polynom_sum_dict)
print(polynom_sum)
