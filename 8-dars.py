#08 BIR NECHTA SHARTLARNI TEKSHIRISH
yosh=int(input("Yoshingiz nechada: "))
if yosh<=6: natija="Siz avtobusga to`lov to`lamaysiz"
elif yosh>=6 and yosh<=50: natija="Siz avtobusga 1400 to`laysiz"
else: natija="               "
print(f" {natija}")
yosh=int(input("yoshingiz nechida: \n>>"))
if yosh<=6: natija=1000
elif yosh<=12: natija=3000
elif yosh<=35: natija=4000
elif yosh<=60: natija=5000
else: natija=3000
print(f"Siz uchun bog\'ga kirish puli  {natija} so\'m")
kun=input("Bugungi kunni kiriting: ")
if kun.lower()=='shanba' or  kun.lower()=='yakshanba': natija0='dam olish'
elif kun.lower()=='dushanba' or kun.lower()=='seshanba' or kun.lower()=='chorshanba' or kun.lower()=='payshanba' or kun.lower()=='juma': natija0='ish'
print(f'Bugun {natija0} kuni')
kun=input('Bugun kun nima>> ')
harorat=float(input("Havo harorati qanday>> "))
if kun.lower()=='shanba' or kun.lower()=='yakshanba' and harorat>=32:
    natija="Qani ketdik cho\'milishga"
else:natija="Uyda qolamiz"
print(f'{natija}')
ovqat=15000
choy=True
salat=False
if choy and salat:
    ovqat=ovqat+10000
elif choy or salat:
    ovqat=ovqat+5000
print(f'Hurmatli mijoz siz {ovqat} so`m to`lov qilishingiz kerak')
ovqat=True
choy=True
salat=True
kompot=False
asorti=False
non=True
summa=0
if ovqat:
    summa=summa+15000
    print("Mijoz ovqat oldi")
if choy:
    summa=summa+4000
    print("Mijoz choy oldi")
if salat:
    summa=summa+8000
    print("Mijoz salat oldi")
if kompot:
    summa=summa+2000
    print("Mijoz kompot oldi")
if asorti:
    summa=summa+7000
    print("Mijoz assorti oldi")
if non:
    summa=summa+6000
    print("Mijoz non oldi")
print(f'Jami summa: {summa}')
menu=['osh','manti','sho`rva','chuchvara']
ovqat=input("Nima ovqat buyurtma qilasiz>>")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi.")
else: print(f'Ushbu taomni buyurtma qilib bo`lmaydi.')
menu2=['osh','manti','sho`rva','chuchvara']
menu1=['osh','manti','sho`rva','chuchvara', 'norin','chuchvara','moshova']
for taom in menu2:
    if taom in menu1:
        print(f'Menyuda {taom}  bor')
    else:print(f"Kechirasiz, menyuda {taom}")
#AMALIYOT

