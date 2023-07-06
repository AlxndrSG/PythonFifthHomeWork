# Создайте список из случайных чисел. Найдите максимальное количество
# его одинаковых элементов.

from random import randint

lst = [randint(0, 10) for _ in range(10)]
print(lst)

set_lst = set(lst)
print(set(lst))

max_count = 0
for i in set_lst:
    if lst.count(i) > max_count:
        max_count = lst.count(i)
print(max_count)
