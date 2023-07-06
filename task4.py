# Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

from random import randint

lst = [randint(0, 10) for _ in range(10)]

print(*lst)
print(*set(lst))

print(list(set(lst))[-2])