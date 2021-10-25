# # FUNKSIYA YARATAMIZ
# def salom_ber():
#     print("Assalomu alaykum")
#
#
# salom_ber()
#
#
# def salom_ber(ism):
#     """Foydalanuvchi ismnini qabul qilib unga salom beruvchi funksiya"""
#     print(f'Assalomu alaykum hurmatli {ism.title()}')
#
#
# salom_ber('dinara')
# def salom_ber(ism):
#     """ Ushbu funksiya foydalanuvchi,
#     ismnini kiritilsa unga salom beradi"""
#     print(f'Assalomu alaykum hurmatli {ism.title()}')
# salom_ber('nodir')
# def FI_(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaradi"""
#     print(f' Sizning to`liq ismingiz {familiya.title()} {ism.title()}')
#
#
# FI_('nodirbek', 'sayfiyev')
# def yosh_hisobla(ism,t_yil):
#     """Foydalanuvchidan ismini va tug`ilgan yilini so`rab yoshini hisoblaydi"""
#     print(f'Hurmatli {ism.title()} sizning yoshingiz {2021-t_yil} da')
#
# yosh_hisobla('nodirbek',1994)
# yosh_hisobla(t_yil=1994,ism='nodirbek')
# def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
#     """Tug`ilgan yili kiritilsa yoshini hisoblaydigan funksiya"""
#     print(f'{joriy_yil-tugilgan_yil} yoshdasiz')
# yosh_hisobla(1994,2020)
# yosh_hisobla(2002)
#AMALIYOT
# def yosh_hisobla(ism,tugilgan_yil, joriy_yil=2021):
#     """foydalanuvchi yoshini hisoblaydi"""
#     print(f'{ism.title()} siz {joriy_yil-tugilgan_yil} yoshdasiz')
# ism=input("Ismingizni kiriting: ")
# yosh=int(input(f'{ism.title()} nechanchi yil tug`ilgansiz: '))
# yosh_hisobla(ism,yosh)
# def kv_kub(son):
#     """sonni kvadrati va kubini hisoblaydi"""
#     print(f'Siz kiritgan {son} sonining Kvadrati {son**2} kubi {son**3}')
# son=int(input("Istalgan sonni kiriting: "))
# kv_kub(son)
# def toq_juft(son):
#     if son%2==0 or son==0:
#         print(f"{son} soni juft son")
#     else:print(f'{son} soni toq son')
# son=int(input("Son bering men uni toq yoji juftligini topaman: "))
# if son<0:
#     print("Bu manfiy son")
# else:toq_juft(son)
# s=0
# for i in range(1,11):
#     for j in range(1,11):
#         s+=1
# print(s)
# A=True
# B=False
# C=True
# D=False
# if (A and B or C and D) and (C and D):
#     print("1")
# else: print('2')
# for i in [1,2,3,4][::1]:
#     print(i, end='-')
# step=3
# for I in range(0,-1,step):
#     print(I)
# s=0
# for i in range(1,376,7):
#     s+=i
# print(s)
# import  random
# T=1000000
# s=0
# for i in range(T):
#     a=random.randint(1,100)
#     b=random.randint(1,100)
#     if (a*b)%2==0:
#         s+=1
# print('%.2f'%(s/T))
# def katta_kichik(x,y):
#     if x<y:
#         print(y)
#     elif x==y:
#         print("teng sonlar")
#     else:print(x)
#
# katta_kichik(4,5)
# katta_kichik(5,5)
# def daraja(x_darajasi,y_soni):
#     """Y soninini X darajaga ko`taradi"""
#     print(f'{y_soni} ni {x_darajasi} darajasi {y_soni**x_darajasi}')
# daraja(4,5)
# daraja(10,2)
# def daraja(y_soni,x_darajasi=2):
#     """Y soninini X darajaga ko`taradi"""
#     print(f'{y_soni} ni {x_darajasi} darajasi {y_soni**x_darajasi}')
# daraja(5)
def func_2_10(son):
    for i in range(2,10):
        if son%i==0:
            print(i, end=', ')
func_2_10(252)

