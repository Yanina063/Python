# Вычислить число c заданной точностью d Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
n = 3.1415926535
d = float(input('Введите число: ')) 

if (d <= 10 ** -1 and d >= 10 ** -10):
    r = round(n, 3)
    print(r)
else:
    print(f'Число  {d} задано не верно')