# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

val = [2, 3, 5, 9, 3]
array_find = []

for index, value in enumerate(val):
    if index % 2 != 0:
        array_find.append(value)
print(sum(array_find)) 
        


