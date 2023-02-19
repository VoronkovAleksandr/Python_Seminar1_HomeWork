# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

def sum_three_num(num: int) -> int:
    i = 0
    sum = 0
    while i < 3:
        sum = sum + (num % 10)
        num //= 10
        i += 1
    return sum

ticket = int(input('Введите номер билета: '))
sum_first_half = sum_three_num(int(ticket//1000))
sum_second_half = sum_three_num(int(ticket%1000))
if sum_first_half == sum_second_half:
    print(f'{ticket} -> yes')
else:
    print(F'{ticket} -> no')