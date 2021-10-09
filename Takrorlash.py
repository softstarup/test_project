ismlar=['ali','vali','anvar','jamila','dlafruz','sattor']
n=0
for mehmon in ismlar:
    print(f'Assalomu alaykum hurmatli {mehmon.title()}')
    n=n+1
print(ismlar)
print(f'Kod {n} marta takrorlandi')
sonlar=list(range(10,101))
for son in sonlar:
    print(f'{son} ning kunbi {son**3} ga teng')
kinolar=[]
for n in range(5):
    kinolar.append(input(f'{n+1} - sevimli kinofiliminggizni kiriting:'))
print(kinolar)
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    print(f"{car.title()}")
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car1 in cars:
    if car1!=car1.title():
        print(f"{car1.title()}")
    else: print("HAFA")
