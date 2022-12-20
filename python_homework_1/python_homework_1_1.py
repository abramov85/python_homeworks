# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

while True:
    try:
        input_day = int(input('input number of day: '))
        if 5 < input_day < 8:
            print('yeah! hollydays')
            break
        elif 0 < input_day < 6:
            print('just another working day...')
            break
        else:
            print('input number greather than 0 and less than 8')
    except:
        print('input a digit')




#