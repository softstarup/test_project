# ismlar=[]
# n=1
# while True:
#     savol=f'{n} - do`stingiz ismni kiriting: '
#     savol2=input(savol)
#     ismlar.append(savol2)
#     javov=input('Yana do`stingizni qo`shasizmi (ha/yo\'q)')
#     if javov=='ha':
#         n=n+1
#     else:break
# print('Sizning do`stlaringiz ismi: ')
# for ism in ismlar:
#     print(ism.title())
# dustlar = {}
# n = 1
# ishora = True
# while ishora:
#     ism = input(f'{n}- do`stingizni ismni kiriting: ')
#     yos = int(input(f'{ism.title()}ning yoshini kiriting: '))
#     dustlar[ism]=yos
#     n += 1
#     javob =input(f'Siz yana boshqa do`stingiz haqida ma`luot qo`shasizmi (ha/yo\'q)')
#     if javob=='yo\'q':
#         ishora=False
# for ism,yosh in dustlar.items():
#     print(f'{ism.title()}ning yoshi {yosh}da')
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'toyota' in cars:
#     cars.remove('toyota')
# print(cars)
# talabalar=['husan','nodir','azizbek','jasur']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=int(input(f'{talaba.title()}ning bahosini kiriting: '))
#     baholangan_talabalar[talaba]=baho
# AMALIYOT
# savat=[]
# n=int(input('Nechta mahsulot buyurtma qilmoqchisiz: '))
# while n:
#     buyurtma=f'Buyturtma qilmoqchi bo`lgan mahsulotingizni kiriting: '
#     qabul=input(buyurtma)
#     savat.append(qabul)
#      n=n-1
# ebozor = {}
# n = int(input("Nechta mahsulot kiritmoqchisiz: "))
# while n:
#     mahsulot = input('Mahsulot nomini kiriting: ')
#     narh = int(input(f'{mahsulot.title()} mahsuloti narhini kiriting: '))
#     ebozor[mahsulot] = narh
#     n = n - 1
# for mah, nar in ebozor.items():
#     print(f'{mah.title()} mahsuloti narxi {nar} so`m')
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
# while buyurtmalar:
#     buyurtma=buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh=mahsulotlar[buyurtma]
#         print(f'{buyurtma.title()} - {narh} so`m')
#     else: print(f'Bizda bunaday {buyurtma} mahsuloti yo`q')