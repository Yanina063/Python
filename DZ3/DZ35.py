# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# k = 8

k = 8
def fib(k):
    if k in [1, 2]:
        return 1
    elif k in [0]:
        return 0
    else:
        return fib(k - 1) + fib(k - 2)
res_2 = []
for e in range(0, k+1):
    res_2.append(fib(e))
print(res_2)


def fib(k):
    if k in [-1, -2]:
        return -1
    else:
        return fib(k + 1) + fib(k + 2)

res_1 = []
for e in range((-1) * k, 0):
    res_1.append(fib(e))
print(res_1)

print(res_1 + res_2)

