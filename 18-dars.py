#17-DARS. MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)
# def summa(*son):
#     summ=0
#     for son1 in son:
#         summ+=son1
#     return summ
# print(summa(1,5,6,8,9,10))
# def summa(x,y,*son):
#     """Kiritilgan sonlar yig`indisi"""
#     return x+y+sum(son)
# print(summa(5,6,9,9,9,10))
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto=avto_info('GM','Malibu',rang='Oqra')
# print(avto)
# def factaryal(*son):
#     """Factarial sonlar"""
#     s=1
#     for i in son:
#         s*=i
#     return s
# print(factaryal(1,2,3))
def talabarlar(ism,familiya,**malumot):
    malumot['ism']=ism
    malumot['familiya']=familiya
    return malumot
talaba=talabarlar('nodirbek','sayfiyev',yosh=25,t_yil=1994,millat='o`zbek')
print(talaba)

