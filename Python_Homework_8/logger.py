from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком формате записать данные: \n\n'
    f'1 Вариант:\n'
    f'{name}\n{surname}\n{phone}\n{address}\n\n'
    f'2 Вариант: \n'
    f'{name};{surname};{phone};{address}\n'
    f'Введите вариант: '))
    while var > 2 or var < 1:
        print('Неправильный ввод.')
        var = int(input('Введите вариант: '))
    if var == 1:
        with open('data_first_variant.csv', 'a') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r') as f:
        data_first = f.readlines()
        print(data_first)
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(data_first_list)
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r') as f:
        data_second = f.readlines()
        print(''.join(data_second))


def delete_data():
    print('Из какого файла хотите уладить данные:\n1 - data_first_variant\n2 - data_second_variant\n')
    del_var = int(input('Ведите номер файла: '))
    while del_var < 1 or del_var > 2:
        del_var = int(input('Ведите номер файла еще раз: '))
    if del_var == 1:
        with open('data_first_variant.csv', 'r') as f:
            del_data_first = f.readlines()
        del_data_first_list = []
        j = 0
        for i in range(len(del_data_first)):
            if del_data_first[i] == '\n' or i == len(del_data_first) - 1:
                del_data_first_list.append(''.join(del_data_first[j:i]))
                j = i
        print(del_data_first_list)
        del_item = int(input(f'Введите номер записи от 1 до {len(del_data_first_list)}: ')) - 1
        while del_item not in range(0, len(del_data_first_list)):
            del_item = int(input(f'Введите номер записи от 1 до {len(del_data_first_list)}: ')) - 1
        del_data_first_list.pop(del_item)
        del_data_first_list.append('\n')
        print(del_data_first_list)
        with open('data_first_variant.csv', 'w') as f:
            f.writelines(del_data_first_list)
    elif del_var == 2:
        with open('data_second_variant.csv', 'r') as f:
            del_data_second = f.readlines()
        del_data_second_list = []
        for i in range(len(del_data_second)):
            if del_data_second[i] != '\n':
                del_data_second_list.append(''.join(del_data_second[i]))
        print(del_data_second_list)
        del_item = int(input(f'Введите номер записи от 1 до {len(del_data_second_list)}: ')) - 1
        while del_item not in range(0, len(del_data_second_list)):
            del_item = int(input(f'Введите номер записи от 1 до {len(del_data_second_list)}: ')) - 1
        del_data_second_list.pop(del_item)
        for i in range(len(del_data_second_list)):
            del_data_second_list[i] += '\n'
        print(del_data_second_list)
        with open('data_second_variant.csv', 'w') as f:
            f.writelines(del_data_second_list)


def change_data():
    print('В каком файле хотите изменить данные:\n1 - data_first_variant\n2 - data_second_variant\n')
    chng_var = int(input('Ведите номер файла: '))
    while chng_var < 1 or chng_var > 2:
        chng_var = int(input('Ведите номер файла еще раз: '))
    if chng_var == 1:
        with open('data_first_variant.csv', 'r') as f:
            chng_data_first = f.readlines()
        chng_data_first_list = []
        j = 0
        for i in range(len(chng_data_first)):
            if chng_data_first[i] == '\n' or i == len(chng_data_first) - 1:
                chng_data_first_list.append(''.join(chng_data_first[j:i]))
                j = i
        print(chng_data_first_list)
        chng_item = int(input(f'Введите номер записи от 1 до {len(chng_data_first_list)}: ')) - 1
        while chng_item not in range(0, len(chng_data_first_list)):
            chng_item = int(input(f'Введите номер записи от 1 до {len(chng_data_first_list)}: ')) - 1
        chng_data_first_list.pop(chng_item)
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        if chng_item == 0:
            chng_data_first_list.insert(chng_item, f'{name}\n{surname}\n{phone}\n{address}\n')
        elif chng_item > 0:
            chng_data_first_list.insert(chng_item, f'\n{name}\n{surname}\n{phone}\n{address}\n')
        chng_data_first_list.append('\n')
        print(chng_data_first_list)
        with open('data_first_variant.csv', 'w') as f:
            f.writelines(chng_data_first_list)
    elif chng_var == 2:
        with open('data_second_variant.csv', 'r') as f:
            chng_data_second = f.readlines()
        chng_data_second_list = []
        for i in range(len(chng_data_second)):
            if chng_data_second[i] != '\n':
                chng_data_second_list.append(''.join(chng_data_second[i]))
        print(chng_data_second_list)
        chng_item = int(input(f'Введите номер записи от 1 до {len(chng_data_second_list)}: ')) - 1
        while chng_item not in range(0, len(chng_data_second_list)):
            chng_item = int(input(f'Введите номер записи от 1 до {len(chng_data_second_list)}: ')) - 1
        chng_data_second_list.pop(chng_item)
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        chng_data_second_list.insert(chng_item, f'{name};{surname};{phone};{address}\n')
        for i in range(len(chng_data_second_list)):
            chng_data_second_list[i] += '\n'
        print(chng_data_second_list)
        with open('data_second_variant.csv', 'w') as f:
            f.writelines(chng_data_second_list)
