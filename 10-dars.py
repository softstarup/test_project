car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['rang'])
talaba_0={'ism':'Sayfiyev Nodirbek','yosh':27,'yil':1994}
print(f"{talaba_0['ism'].title()}, {talaba_0['yil']} - yilda tug`ilgan {talaba_0['yosh']} yoshda")
talaba_0['kurs']=4
talaba_0['fakultet']='informatika'
print(talaba_0)
talaba_1={}
talaba_1['ism']='Odilova Dlafruz'
talaba_1['kurs']=4
talaba_1['yosh']=27
print(talaba_1)
print(f"{talaba_1['ism'].title()}, {talaba_1['kurs']} - kurs talabasi {talaba_1['yosh']}  yoshda")
talaba_2={'ism':'Sayfiyev Nodirbek','yosh':27,'yil':1994}
print(talaba_2)
del  talaba_2['yosh']
print(talaba_2)
telefonlar={
    'Ali':'Iphone X',
    'Vali':'Samsung A10S',
    'Rashid':'LG F25',
    'Sherzod':'Huwai',
}
print(telefonlar)
phone=telefonlar['Ali']
print(f"Alining telefoni {phone}")
phone=telefonlar.get('hasan', 0)
if phone:
    print(f"Alining telefoni {phone}")
else:print('Bunda ism mavjud emas')
otam={'ism':'Rustamov O`ktam','yosh':56,'yil':1971}
onam={'ism':'G`oyibova Dilfuza','yosh':55,'yil':1972}
ukam={'ism':'Sayfiyev Shaxzod','yosh':24,'yil':1997}
singlim={'ism':'Sayfiyeva Dinara','yosh':18,'yil':2002}
rafiqam={'ism':'Odilova Dlafruz','yosh':21,'yil':2000}
print(f"{otam['ism']}, {otam['yil']} -yilda tug`ilgan {otam['yosh']}  yoshda")
print(f"{onam['ism']}, {onam['yil']} -yilda tug`ilgan {onam['yosh']}  yoshda")
print(f"{ukam['ism']}, {ukam['yil']} -yilda tug`ilgan {ukam['yosh']}  yoshda")
print(f"{singlim['ism']}, {singlim['yil']} -yilda tug`ilgan {singlim['yosh']}  yoshda")
print(f"{rafiqam['ism']}, {rafiqam['yil']} -yilda tug`ilgan {rafiqam['yosh']}  yoshda")
taomlar={
    'Ali':'Osh',
    'Vali':'Manti',
    'Salim':'Chuchvara',
    'Ozod':'Xonim'
}
taom=taomlar.get('ali')
print(f"Alining sevimli taomi {taom}")
python_izoh={
    'integer':'Butun son',
    'float':'O`nlik son',
    'string':'Matn',
    'list':'Ro`yxat',
    'tuple':'O`zgarmaydina ro`yxat',
    'del':'O`chirish funsiyasi',
    'insert':'Ro`yxatga istalgan joydan qo`shish',
    'append':'Ro`yxatga qoshish'
}
kalit=input('Kalit so`zni kiriting: ').lower()
print(python_izoh.get(kalit,'Bunday so`z mavjud emas'))
print("""Odami ersang, demagil odami,
Oniki, yo'q xalq g'amidin g'ami""")
print('Men "Dell" notebokni oldim ')
print(f'"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas')

