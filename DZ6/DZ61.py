# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

a = [15, 23, 4, 7, 43, 11, 4]
arr = list(filter(lambda i: a.count(i) == 1, a))
print(arr)