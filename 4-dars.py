# LIST BILAN TANISHAMIZ
mevalar = ['olma', 'anor', 'o`rik', 'shaftoli']  # matnlar
narxlar = [12000, 15000, 3900, 62000]  # sonlar
son_matn = ['anjir', 123, 354, 'bodom']  # son va matndan iborat list
sms = []  # bo`sh list
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
print('Birinchi meva:', mevalar[0].title())
print('Ikkinchi meva: ', mevalar[1].upper())
print('Uchinchi meva: ', mevalar[2].lower())
narxlar = [12000, 13286, 14896, 15000]
print(narxlar[2] + narxlar[3] - narxlar[1])
mashina_modelllari = ['Nexia', 'Damas', 'Trakker', 'Captiva', "Gentra"]
print(mashina_modelllari[-1])
narxlar = [12000, 18000, 10900, 22000]
narxlar[0] = 13000
narxlar[1] = 11000
narxlar[3] = narxlar[3] + 2000
print(narxlar)
mevalar = ['olma', 'anor', 'o`rik', 'shaftoli']
mevalar.append('Tarvuz')
print(mevalar)
cars = []
cars.append('Nexia')
cars.append('Damas')
cars.append('Lasetti')
cars.append('Gentra')
print(cars)
cars.insert(2, 'LADA')
print(cars)
del cars[2]
print(cars)
cars.remove('Nexia')
print(cars)
bozorlik = ['un', 'yog`', 'g`o`sht', 'pomidor', 'banan']
olingan_hasulot = bozorlik.pop(-1)
print("Olingan mahsulotlar: ", olingan_hasulot)
print("Olinmagan mahsulotlar: ", bozorlik)
# amaliy mashqlar
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
ismlar = ['Shuxrat', 'Omon', 'Azizbek']
print('Salom ' + ismlar[0] + ', choyxona bormi?')
print(ismlar[2] + ', choyxonaga boramizmi?0')
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [5210, -2563, 10320, 15982, -852.3235]
print(sonlar)
sonlar.append(256333)
print(sonlar)
sonlar.insert(2, 2356)
print(sonlar)
sonlar[0] = sonlar[-1]
sonlar[1] = sonlar[0] - sonlar[1]
sonlar[-1] = 2356.231
print(sonlar)
t_shaxslar = ["Alisher Navoiy", 'Amir Temur']
z_shaxslar = ["Stiv Jobs", "Xritik Roshan"]
print("Men tarixiy shaxslardan " + t_shaxslar[0] + ' bilan \nzamonaviy shaxslardan esa ' + z_shaxslar[1] + ' bilan \nsuhbat qilishni istar edim')
#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends=[]
friends.append("Shuxrat")
friends.append("Azizbek")
friends.append("Javoxir")
friends.append("G`olib")
print(friends)
friends.remove("Javoxir")
friends.insert(0,'Shaxzod')
friends.insert(1, "Abbos")
friends.insert(5,"Temur")
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(0))
print('\nKelgan mehmonlar: ',mehmonlar,'\n')
t_shaxslar = ["Alisher Navoiy", 'Amir Temur']
z_shaxslar = ["Stiv Jobs", "Xritik Roshan"]
print(f'Men tarixiy shaxslardan {t_shaxslar[0]} bilan \nzamonaviy shaxslardan esa {z_shaxslar[1]}  bilan \nsuhbat qilishni istar edim')