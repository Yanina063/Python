# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#  Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

val = [2, 3, 4, 5, 6]
array_find = []

mid = round(len(val) / 2 + 0.5)
for index, value in enumerate(val):
    if mid == index:
        break
    else:
        array_find.append(value * val[-1 if index == 0 else (index + 1) * -1])
print(array_find) 