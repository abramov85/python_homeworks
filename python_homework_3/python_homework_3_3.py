# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 5, 10.01017, 7.0]
new_list = []
new_round_list = []

for i in my_list:
    is_float_part = 0
    count_decimals = 1
    is_first_iteration = 1
    new_str = str()
    for item in str(i):
        if is_float_part:
            if is_first_iteration and item != '0':
                new_str += item
                is_first_iteration = 0
            elif not is_first_iteration:
                new_str += item
            count_decimals *= 10
        else:
            if item == '.':
                is_float_part = 1
    if new_str.isdigit():
        new_list.append(int(new_str) / count_decimals)

# Вариант попроще, с округлением
for i in my_list:
    if i % 1 != 0:
        new_round_list.append(round((i % 1), 4))

print(my_list)
print(new_list)
print(new_round_list)
print(f'{max(new_list)} - {min(new_list)} = {max(new_list) - min(new_list)}')
print(f'{max(new_round_list)} - {min(new_round_list)} = {round((max(new_round_list) - min(new_round_list)), 4)}')
