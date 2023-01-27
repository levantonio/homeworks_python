""" Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
"""
ticket_number = int(input("Введите номер билета: "))



if ticket_number > 99999 and ticket_number < 1_000_000:
    num1 = (ticket_number // 1_00000)%10
    num2 = (ticket_number // 10000)%10
    num3 = (ticket_number // 1000)%10
    num4 = (ticket_number // 100)%10
    num5 = (ticket_number // 10)%10
    num6 = ticket_number % 10
    sum_left = num1 + num2 + num3
    sum_right = num4 + num5 + num6
    if sum_left == sum_right:
        print(f"{ticket_number} -> Да")
    else:
        print(f"{ticket_number} -> Нет")

else:
    print("Некорректный номер билета")
