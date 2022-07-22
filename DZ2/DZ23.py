# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = 6

def f(n: int):
    i = 1
    dict = {}
    while i <= n:
        if i == 1:
            dict[i] = i + 3
        else:
            dict[i] = dict[i - 1] + 3
        i += 1
    return dict

print(f(N))