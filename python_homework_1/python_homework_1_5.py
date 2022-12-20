# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

while True:
    try:
        x1 = int(input('input x coordinate of first point: '))
        y1 = int(input('input y coordinate of first point: '))
        x2 = int(input('input x coordinate of second point: '))
        y2 = int(input('input y coordinate of second point: '))

        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        print(f'distance between points is {round(distance, 2)})')
        break
    except:
        print('input correct coordinate')
