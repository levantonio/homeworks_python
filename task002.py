""" Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

num = int(input("Введите трехзначное число: "))
if num > 99 and num < 1000:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(f"Сумма цифр трехзначного числа: {sum}")
else:
    print("Неверный ввод")