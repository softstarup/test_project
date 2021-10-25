# # #FUNKSIYADAN ODDIY QIYMAT QAYTARISH
# # def tuliq_ism_yasa(ism,familiya):
# #     """To`liq ism qaytaruvchi funksiya"""
# #     tuliq_ism=f'{ism.title()} {familiya.title()}'
# #     return tuliq_ism
# # ism=tuliq_ism_yasa('nodirbek','sayfiyev')
# # print(ism)
# # #IXTIYORIY ARGUMENTLAR
# # def tuliq_ism_fam_och(ism,familiya,otasining_ismi=''):
# #     """Otasining ismini tekshirib agar busa ism familiya v aotasining ismini bitta maydonga birlashtirib qaytaradi aks holda ism va familiyani uzini birlashtiradi"""
# #     if otasining_ismi:
# #         tuliq_ism=f'{ism} {familiya} {otasining_ismi}'
# #     else: tuliq_ism=f'{ism} {familiya}'
# #     return tuliq_ism.title()
# # ism=tuliq_ism_fam_och("nodirbek",'sayfiyev')
# # ism2=tuliq_ism_fam_och('azizbek','toshtemirov','azimovich')
# # print(ism2)
# # print(ism)
# #FUNKSIYADAN LUG'AT QAYTARAMIZ
# def avto_olam(kompaniya,model,karobka,rang,yil,km,narh=None):
#     """Lug`at qaytaruvchi funksiya"""
#     avto={
#         'kompaniya':kompaniya,
#         'model':model,
#         'karobka':karobka,
#         'rang':rang,
#         'yil':yil,
#         'km':km,
#         'narh':narh
#     }
#     return avto
# # avto1 = avto_olam('GM','Malibu','Avtomat','Qora',2018,102548)
# # avto2 = avto_olam('GM','Gentra','Oq','Mexanika',2016,201568,15000)
# # avtolar=[avto1, avto2]
# # print('online bozordagi mashinalar:')
# # for avto in avtolar:
# #     if avto['narh']:
# #         narh=avto['narh']
# #     else: narh='Nomalum'
# #     print(f'Kompaniya: {avto["kompaniya"]} \n Model: {avto["model"]} \n Karobka: {avto["karobka"]} \n Rang: {avto["rang"]} \n Yili: {avto["yil"]} \n Yurgam masofasi: {avto["km"]} km \n Narhi: {narh} $')
# #FUNKSIYADAN RO'YXAT QAYTARAMIZ
# # def oraliq(min,max):
# #     """sonlar oraligi`ni ro`yxat qilib qaytaradi"""
# #     sonlar=[]
# #     if min<max:
# #         while min<max:
# #             sonlar.append(min)
# #             min=min+1
# #     elif max<min:
# #         while max<min:
# #             sonlar.append(min)
# #             min=min-1
# #     return sonlar
# # print(oraliq(5,25))
# #
# # print(oraliq(10,5))
#
# print("Avtomobillar ro`yxatini tuzamiz:")
# avtolar=[]
# n=int(input("Sizda mavjud avtomobillar soni: "))
# i=1
# while n:
#     print(f"{i}- avtomashina haqida malumotlarni kiritamiz:\n ############################################################\n")
#     kompaniya=input("Kompaniya: ")
#     model=input("Model: ")
#     karobka=input("Karobka: ")
#     rang=input("Rangi: ")
#     yil=input("Ishlab chiqarilgan yili:" )
#     km=int(input("Yurgan masofasi (km): "))
#     narh=int(input("Narhi($): "))
#     avtolar.append(avto_olam(kompaniya,model,karobka,rang,yil,km,narh))
#     i+=1
#     n-=1
#
# for avts in avtolar:
#     print(f"{avts['rang']} rangli  {avts['model']} rusumli avtomashinaning narxi: {avts['narh']}$")
#
# AMALIYOT
# def foydalanuvchi(ism,fammiliya,tugilgan_yili,tugilgan_joyi,yashash_manzili,e_mail=None,telefon=None):
#
#     mijoz={
#         'ism':ism,
#         'familiya':fammiliya,
#         'tugilgan_yili':tugilgan_yili,
#         'tugilgan_joyi':tugilgan_joyi,
#         'yashash_manzili':yashash_manzili,
#         'e_mail':e_mail,
#         'telefon':telefon,
#         'yoshi':2021-tugilgan_yili
#     }
#     return mijoz
# foydalanuvchilar=[]
# n=int(input("Men nechta foydalanuvchi malumotlarni kiritaman soni: "))
# i=1
# while n:
#     print(f"{i}- foydalanuvchi ma`lumotlarni kiriting:\n ######################################################################")
#     ism=input("Foydalanuvchi ismi:*  ")
#     familiya=input("Foydalanuvchi familiyasi:* ")
#     tugilgan_yili=int(input("Foydalanuvchi tug`ilgan yili:* "))
#     tugilgan_joyi=input("Foydalanuvchi tug`ilgan joyi:* ")
#     yashash_manzili=input("Foydalanuvchi yashash manzili:* ")
#     e_mail=input("Foydalanuvchi e-mail: ")
#     telefon=input("Foydalanuvchi telefon: ")
#     foydalanuvchilar.append(foydalanuvchi(ism,familiya,tugilgan_yili,tugilgan_joyi,yashash_manzili,e_mail,telefon))
#     n-=1
#     print(f"###################################################################### \n {i}- foydalanuvchi ma`lumotlari kiritildi: \n")
#     i += 1
# for foyda in foydalanuvchilar:
#     print(f' {foyda["ism"].title()} {foyda["familiya"].title()} {foyda["tugilgan_yili"]} - yilda tug`ilgan. '
#           f'Hozirda {foyda["yoshi"]} yoshda va yashash mazili: {foyda["yashash_manzili"]}')
# def eng_katta(a,b,c):
#     if a<=b or a<=c:
#         if c<=b:
#             print(f'{b} soni en katta son')
#         else:
#             print(f'{c} soni en katta son')
#     else:print(f'{a} soni en katta son')
#
# eng_katta(5,3,9)
# eng_katta(10,10,10)
#
# def kattasi(a,b,c):
#     max=a
#     if max<=b:
#         max=b
#     if max<=c:
#         max=c
#     print(max)
#
# kattasi(5,3,7)
# def aylana_rad(a,pi=3.14159):
#     aylana={
#         'radisi':a,
#         'diametri':2*a,
#         'Uzunligi':2*pi*a,
#         'yuzi':pi*(a**2)
#
#     }
#     return aylana
# print(aylana_rad(5))
# def tub_sonlar_top(a,b):
#     tub_sonlar=[]
#     for n in range(a,b+1):
#         tub=True
#         if n==1:
#             tub=False
#         elif n==2:
#             tub=True
#         else:
#             for x in range(2,n):
#                 if n%x==0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# print(tub_sonlar_top(1,21))
# def fibonachchi(a):
#     sonlar=[]
#     for x in range(a):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# print(fibonachchi(10))
