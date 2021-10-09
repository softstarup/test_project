#AMALIYOT
son=int(input("Juft son kiriting: "))
if son%2==0:
    print('Bu son juft')
else: print ('Bu son toq')
yosh=int(input('Marhamat yozingizni kiriting:'))
if yosh<=4 or yosh>=60:
    natija=0
elif yosh<=18:
    natija=10000
elif yosh>18:
    natija=20000
print(f'Muzeyga kirish {natija} so\'m')
son1=int(input("Birinchi sonni kiriting: "))
son2=int(input("ikkinchi sonni kiriting: "))
if son1>son2:
    print(f'{son1} - soni {son2} dan katta')
elif son1==son2:
    print(f'{son1} - son {son2} ga teng')
else:print(f'{son1} - soni {son2} dan kichik')
mahsulotlar=['banan','uzum','olma','balgar','qovun','tarvuz','bodring','pomidor','shaftoli','nok','olcha']
savat=[]
for i in range(5):
    savat.append(input(f"{i+1} - mahsulotni kiriting: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f'{mahsulot} do`konimizda bor')
    else:print(f'{mahsulot} do`konimizda yoq')
son=int(input('Do`konga nechta mahsulot kiritmoqchisiz: '))
dukon=[]
mavjud=[]
mavjud_emas=[]
mahsulotlar=['banan','uzum','olma','balgar','qovun','tarvuz','bodring','pomidor','shaftoli','nok','olcha']
for k1 in range(son):
    dukon.append(input(f'{k1+1} -mahsulotni kiriting: '))
for mahsulot in mahsulotlar:
    if mahsulot in dukon:
        mavjud.append(mahsulot)
    else:mavjud_emas.append(mahsulot)
if mavjud_emas:
    print('Siz so\'ragan quyidagi mahsulotlar do\'konimizda yo`q')
    for mahsulot in mavjud_emas:
        print(mahsulot,' ')
else: print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
users=['ahmad','anvar','softstarup','filest','aziz','bekki']
login=input('Loginingizni kiriting:')
if login.lower() in users:
    print('Login band, yangi login tanlang!')
else: print(f'Xush kelibsiz, {login.title()}')
son=int(input("Istalgan butun sonni kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f' {son} soni {n} ga qoldiqsiz bo`linadi')
