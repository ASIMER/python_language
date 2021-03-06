#task1------------------------------------------------------------
"""
Умова: Дано два цілих числа. Вивести найменше з них.

Вхідні дані: користувач вводить ціле число

Вихідні дані: вивести ціле число
"""

a=int(input())
b=int(input())
if a>=b:
    print(b)
else:
    print(a)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Вивести результат функціїsign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
"""

x=int(input())
if x>0:
    print(1)
elif x==0:
    print(0)
else:
    print(-1)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Умова: Дано три цілих числа. Вивести найменше з них.

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""

a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".

Рік високосний, якщо виконується хоча б одна з умов:

рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
рік завжди високосним, якщо його номер ділиться на 400 без остачі
Вхідні дані: ціле число, що вводить користувач

Вихідні дані: вивести текстовий рядок.
"""

y=int(input())
if (y%4==0) and (y%100!=0) or (y%400==0):
    print("LEAP")
else:
    print("COMMON")

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""

a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print(3)
elif a==b or b==c or c==a:
    print(2)
else:
    print(0)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1==b1:
    if a2!=b2:
        print("YES")
elif a2==b2:
    if a1!=b1:
        print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
black1=False
black2=False
white1=False
white2=False
#1 color=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if a1%2!=0:
    if b1%2!=0:
        black1=True
    else:
        white1=True
else:
    if b1%2!=0:
        white1=True
    else:
        black1=True
#2 color=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if a2%2!=0:
    if b2%2!=0:
        black2=True
    else:
        white2=True
else:
    if b2%2!=0:
        white2=True
    else:
        black2=True
#color check=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if black1==True and black2==True or white1==True and white2==True:
    print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

from math import fabs
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
r1=fabs(a1-b1)
r2=fabs(a2-b2)
if r1>1 or r2>1:
    print("NO")
else:
    if a1==b1:
          if a2!=b2:
            print("YES")
    elif a2==b2:
        if a1!=b1:
            print("YES")
    else:
        if r1==r2:
            print("YES")
        else:
            print("NO")

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

from math import fabs
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
r1=fabs(a1-b1)
r2=fabs(a2-b2)
if r1==r2:
    print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

from math import fabs
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
r1=fabs(a1-b1)
r2=fabs(a2-b2)
if a1==b1:
    if a2!=b2:
        print("YES")
elif a2==b2:
    if a1!=b1:
        print("YES")
else:
    if r1==r2:
        print("YES")
    else:
        print("NO")

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Умова: Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

from math import fabs
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1==(b1+2) or b1==(a1+2):
    if a2==(b2+1) or b2==(a2+1):
        print("YES")
    else:
        print("NO")
elif a2==(b2+2) or b2==(a2+2):
    if a1==(b1+1) or b1==(a1+1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.

Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""

n=int(input())
m=int(input())
k=int(input())
if k<n*m and (k%m==0 or k%n==0):
    print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


