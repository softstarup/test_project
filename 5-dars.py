#05 RO'YXATLAR BILAN ISHLASH
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)
cars = ['Bmw','mercedes benz', 'Volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
print(sorted(mehmonlar, reverse=True))
sonlar=[12,98,31,56,42,15,32,11,9,8,16]
sonlar.sort()
print(sonlar)
print(sorted(sonlar, reverse=True))
mevalar=['Banan','Olma','Shaftoli', 'Kakos','Anor','Anjir']
print(mevalar)
mevalar.reverse()
print(mevalar)
mevalar=['Banan','Olma','Shaftoli', 'Kakos','Anor','Anjir']
print('Elementlar soni:', len(mevalar))
sonlar=list(range(0,21))
print(sonlar)
juft_sonlar=list(range(0,20,2))
toq_sonlar=list(range(1,20,2))
print(f'{juft_sonlar}\n{toq_sonlar}')
son2=list(range(10))
print(son2)
narxlar=[12131,13210,12132,15236,15632,15423,16523]
arzon=min(narxlar)
qimmat=max(narxlar)
jami=sum(narxlar)
print("Eng arzon narx:",arzon,'Eng qimmat narx: ',qimmat, "Jami: ",jami)
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
mers=cars[0:3]
print(mers)
print(cars[2:5])
print(cars[:4])
print(cars[2:])
sonlar=[1,2,3,4,5,6,7,8]
sonlar2=sonlar
sonlar2.append(9)
sonlar2.append(10)
print(f'Sonlar: {sonlar},\nSonlar2: {sonlar2}')
sonlar=[1,2,3,4,5,6,7,8]
sonlar2=sonlar[:]
sonlar2.append(9)
sonlar2.append(10)
print(f'Sonlar: {sonlar},\nSonlar2: {sonlar2}')
tomonlar=(12,14,52)
print(tomonlar)
print(f'A tomon: {tomonlar[0]} \nB tomon: {tomonlar[1]} \nC tomon: {tomonlar[2]}')
mashinalar=('Nexia','Damas','Lasetti','Tico','Captiva','Malibu','Matiz')
mashinalar=list(mashinalar)
mashinalar.append('Jiguli')
mashinalar.insert(0,'Ravon')
mashinalar.remove('Tico')
mashinalar[5]='Best Matiz'
print(mashinalar)
#uyga Vazifa
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
print("\nUYGA VAZIFA\n")
davlatlar=['O`zbekiston','Qozog`iston','Tojigiston','Turkmaniston','Avg`oniston','Russia','AQSH','Canada','Turkiya']
print(davlatlar)
#Ro'yxatning uzunligini konsolga chiqaring
print(f'Davlatlar ro`yxati soni: {len(davlatlar)} ta')
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(f'Sorted funsiyasida ro`yxatni tartiblaymiz: {sorted(davlatlar)}')
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(f'Sorted funksiyasi yordamida ro`yxatni teskari saralaymiz: {sorted(davlatlar, reverse=True)} ')
#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_son=list(range(120,1201,2))
print(juft_son)
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
jami=sum(juft_son)
print(f'Ro`yxatdagi sonlar yig`indisi: {jami}')
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
katta_son=max(juft_son)
kichik_son=min(juft_son)
ayirma=katta_son-kichik_son
print(f'Ro`yxatdagi katta son: {katta_son} dan kichik son: {kichik_son} ni ayirmasi: {ayirma}')
#Ro'yxatdagi elementlar sonini hisoblang
print(f'Ro`yxatdagi elementlar soni: {len(juft_son)}')
print('Boshidan 20ta son ',juft_son[:20])
print('Oxiridan 20 ta son ',juft_son[-20:])
print('O`rtasidan 20 tason', juft_son[270:290])
#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar=['Norin','Manti','Kabob','Somsa','Chuchvara']
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta=taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.append('Tuxum')
nonushta.append('Maloko')
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(f'Taomlar ro`yxati: {taomlar} \nNonushtaga taomlar ro`yxati: {nonushta}')
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta=tuple(nonushta)
print(nonushta)