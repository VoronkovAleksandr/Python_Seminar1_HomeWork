# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# 
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"

s = int(input('Введите S: '))

if s%6 == 0:
    petya = int(s/6)    
    katya = int(petya*4)
    
    text = f'{s} -> {petya} {katya} {petya}'
else:
    text = 'Неверное S'

print(text)

