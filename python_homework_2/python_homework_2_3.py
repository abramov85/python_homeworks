# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

input_list = [12, 43, 773, 'qaw', '[[]]', 'low', 3, 998, 'croud', 'symbols']
index_list = []
output_list = []

for i in range(len(input_list)):
    index_list.append(i)

for i in range(len(input_list)):
    output_list.append(input_list[index_list.pop(randint(0, len(index_list) - 1))])

print(input_list)
print(output_list)