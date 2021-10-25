"""Kutubxonam mening"""
def avto_info(kompaniya,model,rangi,ish_yil,masofa,narh=None):
    """Malumotlarni lug`at ko`rinishida qaytaradigan funksiya"""
    avto ={
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'ishlab_chiqarilgan_yili':ish_yil,
        'masofa':masofa,
        'narh':narh
    }
    return avto
def avto_kirit():
    """avto_info funksiyasi yordamida listga malumotlarni lug`at ko`rinishida kiritadi"""
    n=int(input("Nechta mashina haqida ma`lumot kiritmoqchisiz: "))
    avto =[]
    while n:
        print('Quyidagi malumotlarni kiriting:', end=' ')
        kompaniya=input('Kompaniya nomi: ')
        model=input('Modeli: ')
        rangi=input('Rangi: ')
        ish_yil=input('Ishlab chiqarilgan yili: ')
        masofa=input('Yurgan masofasi: ')
        narh=input('Narh:')
        avto_info(kompaniya,model,rangi,ish_yil,masofa,narh)
        n-=1
def avto_print(avto_info):
    """Avtomobillar haqidagi ma`lumotlar saqlangan lug`atni konsolga chiqaruvchi"""
    print(f"Kompaniya: {avto_info['kompaniya'].upper()}, Model: {avto_info['model'].upper()} "
          f"Rangi: {avto_info['rang'].title()}, Ishlab chiqarilgan yil: {avto_info['ishlab_chiqarilgan_yili']} "
          f"Bosib utgan masofa: {avto_info['masofa']}, Narhi: {avto_info['narh']}$")
