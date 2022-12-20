# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

while True:
    try:
        x = float(input('input x coordinate: '))
        y = float(input('input y coordinate: '))
        if x > 0 and y > 0:
            print(f'({x},{y}) - is 1 quarter')
            break
        elif x < 0 and y > 0:
            print(f'({x},{y}) - is 2 quarter')
            break
        elif x < 0 and y < 0:
            print(f'({x},{y}) - is 3 quarter')
            break
        elif x > 0 and y < 0:
            print(f'({x},{y}) - is 4 quarter')
            break
        else:
            print('input x and y not equal 0')
    except:
        print('input only numbers')
