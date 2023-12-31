# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exp(a, b):
    if b == 0:
        return 1
    if (b == 1):
        return a
    if b != 1:
        return (a * exp(a, b-1))

a = int(input("Введите число:"))
b = int(input("Введите степень:"))
print(f'Результат возведения числа {a} в степень {b} ->', exp(a, b))
