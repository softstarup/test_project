#06  FOR TAKRORLASH OPERATORI
mehmonlar=['Shuxrat', 'Abbos','Ali','Azizbek','Anvar','Farrux','Jumamurod','Jasur']
for mehmon in mehmonlar:
    print(mehmon)
for taklif in mehmonlar:
    print(f'\nHurmatli {taklif} sizni 20-dekabr kuni yoziladigan dasturxonimizga taklif etamiz')
    print('Hurmat ehtirom bilan Sayfiyevlar oilasi\n')
sonlar=list(range(1,11))
for son in sonlar:
    print(f'{son} ning kvadrati {son**2} ga teng bo`ladi.')
sonlar=list(range(1,11))
son_daraja=[]
for son in sonlar:
    son_daraja.append(son**2)
print(sonlar)
print(son_daraja)
dustlar=[]
print('5 ta eng yaqin do`stingiz kim?')
for n in range(5):
    dustlar.append(input(f"{n+1}-do`stingizni ismini kiriting: "))
print(dustlar)
#Amaliyot
#Kamida 10 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar=[]
print('10 ta ism kiritib olamiz.')
for i in range(10):
    ismlar.append(input(f'{i+1}-ismni kiriting: '))
for ism in ismlar:
    print(f"Assalomu alaykum {ism} aka yaxshimisiz yaxshi yuribsizmi \n")
print(f'Kod {i+1} marta takrorlandi')
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_son=list(range(11,100,2))
for son in toq_son:
    print(f'{son**3}')
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar=[]
print('Eng sevimli 5 ta kinolaringizni kiriting:\n')
for i in range(5):
    kinolar.append(input(f'{i+1}- kino nomini kiriting: '))
print(kinolar)
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
ismlar=[]
soni=int(input('Bugun necha kishi bilan suhbat qildingiz: \n>>>'))
for ism in range(soni):
    ismlar.append(input(f'{ism+1}- suhbatlashgan odamingiz ismi: '))
print(ismlar)
