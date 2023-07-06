# Создайте список из случайных чисел. Найдите номер его последнего
# локального максимума (локальный максимум — это элемент, который больше
# любого из своих соседей).

from random import randint

lst = [randint(0, 10) for _ in range(10)]

print(*lst)

local_max = 0
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        local_max = lst[i]
print(local_max)
