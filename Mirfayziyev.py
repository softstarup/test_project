kurs = int(input("Qaysi kursni almashtirmohchisiz: Dollar -1 , Rubl - 2 , So`m - 3 \n   "))
if kurs == 1:
    d = int(input('Qaysi kursga o`tmohchisiz: Rubl - 1 , So`m - 2 \n '))
    money = int(input('Almashtirish kerak bo`lgan valyutani  kiriting : '))
    if d == 1 :
        rubl=int(input('Rubl kursini kiriting: '))
        rubl1=money*rubl
        print(round(rubl1,2),' Rubl ')
    elif d == 2:
        dollar=int(input('Dollar kursini kiriting: '))
        som1=dollar*money
        print(round(som1,2),' So`m ')


elif kurs == 2:
    r = int(input('Qaysi kursga o`tmohchisiz: Dollar - 1 , So`m - 2 \n'))
    money = int(input('Almashtirish kerak bo`lgan valyutani  kiriting : '))
    if r == 1:
        rubl = int(input('Rubl kursini kiriting: '))
        dollar1 = money/rubl
        print(round(dollar1,2),'Dollar ')
    elif d == 2:
        som = int(input('So`m kursini kiriting: '))
        som1 = money*som
        print(round(som1,2), ' So`m ')

else:
    s = int(input('Qaysi kursga o`tmohchisiz: Rubl - 1 , Dollar - 2  \n '))
    money = int(input('Almashtirish kerak bo`lgan valyutani  kiriting : '))
    if s == 1:
        rubl = int(input('Rubl kursini kiriting: '))
        som1 = money/rubl
        print(round(som1,2),'Rubl ')
    elif s == 2:
        dollar = int(input('Dollar kursini kiriting: '))
        som1 = money/dollar
        print(round(som1,2), ' Dollar ')
son = int(input("Istalgan butun sonni kiriting: "))
son = str(son)
i = len(son)
k = len(son)
for sons in son:
    if i % 3 != 0:
        print(sons, end='')
        i = i - 1
    elif i % 3 == 0:
        if i == k:
            print(sons, end='')
        else:
            print(f'.{sons}', end='')
        i = i - 1
