# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: 
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('введите X -'))
y = int(input('введите Y -'))
if x > 0 and y > 0:
    print('это I четверть плоскости')
elif x < 0 and y > 0:
    print('это II четверть плоскости')    
elif x > 0 and y < 0:
    print('это III четверть плоскости ')
elif x < 0 and y < 0:
    print('это IV четверть плоскости ')
else:
    print('данные введены не корректно')