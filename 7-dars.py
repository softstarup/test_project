#07 IF-ELSE
avtolar=['nexia','lasetti','tico','captiva','ravon','matiz','damas']
for avto in avtolar:
    if avto=='captiva':
        print(avto.upper())
    else:print(avto.title())
ism='Ali'
if ism.lower()=='ali':
    print("To`g`ri")
ism=input('Marhamat loginni kiriting:\n>>>')
if ism.lower()!='ali':
    print('Uzr kechirasiz siz noto`g`ri login kiritdingiz:')
else:print(f'Salom {ism}')
son=int(input(f'12*12 javo nimaga teng: '))
if son!=144:
    print(f'Uzr siz bergan {son} javobi xato')
else:print(f'Siz to`gri javob berdingiz. Javob {son}')
yil=int(input('Tug`ilgan yilingizni kiriting: '))
if 2021-yil<18:
    print(f'Sizning yoshingiz {2021-yil} da ekan')
    print("Kechirasiz sizga kirish mumkin emas!")
else:print("Xush kelibsiz!")
yosh=int(input("Yoshingiz nechida: "))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
x=45
y=35
print('x>y') if x>y else print('x<y')
#Amaliyot
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini
# katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car=='gm': print(car.upper())
    else:print(car.title())
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
print('\n')
for car in cars:
    if car!='gm': print(car.title())
    else:print(car.upper())
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini
# ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
login=input("Loginni kiriting:")
if login.lower()=='admin':
    print(f'Xush kelibsiz {login.title()}. Foydalanuvchilar ro`yxatini ko`rasizmi?')
else:print(f'Xush kelibsiz {login.title()}!')
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print('Marhamat ikkita son kiriting \n')
a1=int(input('Birinchi sonni kiriting: '))
a2=int(input("Ikkinchi sonni kiriting: "))
if a1==a2: print('Sonlar teng ekan.')
else:print('Kiritgan sonlariz teng emas.')
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
print('Istalgan sonni kiriting:')
son=int(input('Sonni kiriting:'))
if son>0: print('Bu son musbat son')
else:print("Bu son manfiy son")
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
print('Istalgan sonni kiriting:')
son=int(input("Sonni kiriting: "))
if son>=0: print(f'Siz kiritgan sonning ildizi: {int(son**(1/2))}')
else:print('Musbat sonni kiriting:')