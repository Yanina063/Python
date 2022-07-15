# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

from tkinter import Y


x1 = int(input('введите X1 -'))
y1 = int(input('введите Y1 -'))
x2 = int(input('введите X2 -'))
y2 = int(input('введите Y2 -'))

x = (x1-x2)**2
y = (y1-y2)**2
print(x,y)
z = x + y
sgrt = round(z ** (0.5), 2)
print (sgrt)