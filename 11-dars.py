talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
print(talaba_0.items())
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
for kalit, qiymat in talaba_0.items():
    print(f'Kalit: {kalit}')
    print(f'Qiymat: {qiymat}\n')
telefonlar={
    'ali':'Iphone X',
    'vali':'Samsung A10S',
    'jamshid':'Huwai P30',
    'shuxrat':'Honor LITE'
}
for keys,qiymat in telefonlar.items():
    print(f'{keys.title()}ning telefoni "{qiymat}"')
mahsulotlar={
    'olma':2000,
    'anor':3000,
    'anjir':4000,
    'shaftoli':5000,
    'uzum':6000
}
print('Do\'kondagi mahsulotlar ro\'yxati')
for mah in mahsulotlar.keys():
    print(mah.title())
print("\n")
ahsulotlar={
    'olma':2000,
    'anor':3000,
    'anjir':4000,
    'shaftoli':5000,
    'uzum':6000
}
bozorlik=['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} so`m')
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f'Iltimos do`koningizga {buyum.title()} ham olib keling')
print("\n Do`konimizdagi mahsulotlar \n")
for tovar in sorted(mahsulotlar):
    print(tovar.title())
print(telefonlar.values())
for tel in telefonlar.values():
    print(tel)
telefons = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

print('\nFoydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefons.values():
    print(tel)
print('\nFoydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tels in set(telefons.values()):
    print(tels)
print('\n+++++++++++++++++++++++++++++++++\n')
python_izoh={
    'strip':'Ikki tomonidan bo`sh joyni olib tashlaydi',
    'rstrip':'Oxiridan bo`sh joyni olib tashlaydi',
    'lstrip':'Boshidan bo`sh joyni olibtashladi',
    'for':"sikl operatori",
    'integer':'Butun son',
    'float':'O`nlik son',
    'if':'shrt operatori',
    'else':'inkor operatori',
    'list':'Ro`yxat',
    'tuple':'O`zgarmaydigan ro`xat'
}
for k,q in sorted(python_izoh.items()):
    print(f'Kalit: {k}')
    print(f'Izoh: {q}')
    print('##################################################')
davlatlar={
    'O`zbekriton':'Toshkent',
    'Rossiya':'Moskva',
    'Xitoy':'Pekin',
    'AQSH':'Vashington',
    'Turkiya':'Istambul',
    'Fransiya':'Parij'

}

for d,p in sorted(davlatlar.items()):
    print(f'Davlat {d}, Poytaxti {p}')
print("+++++++++++++++++++++++++++++++++++++++++")
print("\nDavlatlar")
for dav in sorted(davlatlar.keys()):
    print(dav.upper())
print("\nPoytaxtlar")
for poy in sorted(davlatlar.values()):
    print(poy.upper())

davlats={
    'Uzbekiston':'Toshkent',
    'Rossiya':'Moskva',
    'Xitoy':'Pekin',
    'AQSH':'Vashington',
    'Turkiya':'Istambul',
    'Fransiya':'Parij'

}
davlat=input("Istalgan davlatni kiriting mensizga uni poytaxtini aytaman: ")
cap=davlats.get(davlat.title())
if cap==None:
    print("Ushbu davlat haqida menda ma`lumot yo`q")
else:print(f'Siz kiritgan {davlat.title()} davlati poytaxti {davlats[davlat.title()]}')
menu_taom={
    'osh':30000,
    'kabob':70000,
    'manti':25000,
    'xonim':30000,
    'salonka':30000
}
menu_boshqa={
    'oliviya':25000,
    'karam':10000,
    'gurman':24000,
    'fransuski':22000,
    'sezer':26320
}
narx=0
son=int(input("Nechta taom buyurmoqchisiz: "))
buyurtmataom=[]
for n in range(son):
    buyurtmataom.append(input(f'{n+1}- taomni kiriting: ').lower())
son_salat=int(input("Nechta salat buyurmoqchisiz: "))
buyurtmaboshqa=[]
for i in range(son_salat):
    buyurtmaboshqa.append(input(f'{i+1}-salatni kiriting: '))
for buyutma in buyurtmataom:
    if buyutma in menu_taom:
        print(f'{buyutma.title()}   {menu_taom[buyutma]} so`m')
        narx=narx+menu_taom[buyutma]
for buyutma in buyurtmaboshqa:
    if buyutma in menu_boshqa:
        print(f'{buyutma.title()}   {menu_boshqa[buyutma]} so`m')
        narx=narx+menu_boshqa[buyutma]
print(f'Siz jami {narx} so`m to`lov qilasiz!')