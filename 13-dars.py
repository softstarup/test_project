#13-DARS. while TSIKLI
# ism=input(f"Isminggiz nima: ")
# print(f'Sizning ismingiz {ism.title()}')
# ism2=input("Ismingiz nima? ")
# savol=f'Salom {ism2.title()} yoshingiz nechida: '
# yosh=int(input(savol))
# ism3=input('Ismingiz nima: ')
# savol2= f"Salom {ism3.title()} yoshingiz nechida: "
# yosh2=input(savol2)
# yosh2=int(yosh2)
# heigt=input("Bo`yingiz necha metr: ")
# heigt=float(heigt)
# #while TSIKLI BILAN TANISHAMIZ
# son=0
# while son<=10:
#     print(son, end=', ')
#     son=son+1
# print('\nIstalgan sonni kvadratini topaman:')
# savol="Istalgan sonni kiriting: "
# savol +="Chiqish uchun 'exit' yozuvini kiriting: "
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2)
# print('\n')
# print("Kiritilgan sonni kvadratini qaytaruvchi dastur:")
# son='Istalgan sonni kiriting '
# son +='dasturdan chiqish uchun exti deb yozing: '
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#         print("Dasturdan muvofiqatli chiqish yuz berdi:")
#     else:print(float(qiymat)**2)
# print("Kritilgan sonni kvadratini qaytaruvchi dastur:")
# savol="Istalgan sonni kiriting:"
# chiqish='Chiqish uchun exit deb yozuv kiriting:'
# while True:
#     print(chiqish)
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break
#     else:print(float(qiymat)**2)
# sonlar=list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else: print(f'{son} sonining kvadrati {son**2} ga teng')
# print("###############################################################")
# for son in sonlar:
#     if son ==5:
#         continue
#     else:print(f'{son} sonining kvadrati {son**2} ga teng')
# son=0
# while son<10:
#     son +=1
#     if son%2==0:
#         continue
#     else:print(son, end=", ")
# print('\n')
#AMALIYOT
# kitoblar=[]
# son=1
# savol= " kitobingizni kiriting:"
# while True:
#     qiymat=input(f"{son}-{savol}")
#     son +=1
#     if qiymat=='stop':
#         break
#     else:kitoblar.append(qiymat)
# for kitob in kitoblar:
#     print(kitob, end=', ')
savol="Muzeyga kirish uchun yoshingizni kiriting:"
narh=0
while True:
    qiymat=input(savol)
    if qiymat=='stop' or qiymat=='quit':
        break
    yosh=int(qiymat)
    if yosh<=7 and yosh>0:
        narh=5000
    elif yosh>7 and yosh<=18:
        narh=10000
    elif yosh>18 and yosh<=65:
        narh=15000
    elif yosh>65 and yosh<=120:
        narh=0
if narh==0:
    print("Sizga muzeyga kirish bepul")
else:print(f"Sizga muzeyga kirish {narh} so`m")