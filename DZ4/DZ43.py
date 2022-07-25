# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

a = [15, 23, 4, 7, 43, 11, 4]
b = []

for index, i in enumerate(a):
    doublicate = False
    for index_2, j in enumerate(a):
        if(index == index_2):
            continue
        if(i == j):
            doublicate = True
    if(doublicate == False):
        b.append(i)
            
print(b)