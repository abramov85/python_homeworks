# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    try:
        quarter_num = int(input('input quarter number (from one to four): '))
        if quarter_num == 1:
            print(f'1 quarter: x > 0 and Y > 0')
            break
        elif quarter_num == 2:
            print(f'2 quarter: x < 0 and Y > 0')
            break
        elif quarter_num == 3:
            print(f'3 quarter: x < 0 and Y < 0')
            break
        elif quarter_num == 4:
            print(f'4 quarter: x > 0 and Y < 0')
            break
        else:
            print('only integer from 1 to 4')
    except:
        print('input only integer')
