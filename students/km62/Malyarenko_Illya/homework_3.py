#task1------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""

#defaults-----------------------------
i = 1
result = 1
#Input--------------------------------
number=int(input())
#main---------------------------------
for i in range(number):
    result= result*(i+1)
#output-------------------------------
print(result)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
"""

#defaults-----------------------------
i = 0
result = 0
fact=1
#Input--------------------------------
number=int(input())
#main---------------------------------
for i in range(1, number+1):
    fact*=i
    result+= fact
#output-------------------------------
print(result)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""

#defaults-----------------------------
zero_counter = 0
number_place = 1
#Input--------------------------------
number_amount=int(input())
#main---------------------------------
for i in range(number_amount):
    number_place=float(input())
    if number_place==0:
        zero_counter+=1
#output-------------------------------
print(zero_counter)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""

#defaults-----------------------------
numbers=0
number=0
string=""
#Input--------------------------------
numbers=int(input())
#main---------------------------------
for i in range(numbers):
    number+=1
    string+=str(number)
    print(string)

#-----------------------------------------------------------------

