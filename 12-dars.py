car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
cars=[car0,car1,car2]
for car in cars:
    print(f"Rusumi {car['model'].title()} rangi {car['rang'].title()} ishlab chiqarilgan yili {car['yil']} Narxi:{car['narh']} Yurgan yuli: {car['km']}  Karobka: {car['korobka'].title()} ")
print("\n")
malibus=[]
for n in range(10):
    if n<=3:
        new_car = {  # har bir yangi mashina uchun lug'at yaratamiz
            'model': 'malibu',
            'rang': 'Oq',  # rangi noaniq
            'yil': 2021,
            'narh': None,  # narhi belgilanmagan
            'km': 12563,
            'korobka': 'avto'
        }
        malibus.append(new_car)
    elif n<=6:
        new_car = {  # har bir yangi mashina uchun lug'at yaratamiz
            'model': 'malibu',
            'rang': 'Yashil',  # rangi noaniq
            'yil': 2020,
            'narh': None,  # narhi belgilanmagan
            'km': 13205,
            'korobka': 'avto'
        }
        malibus.append(new_car)
    else:
        new_car = {  # har bir yangi mashina uchun lug'at yaratamiz
            'model': 'malibu',
            'rang': None,  # rangi noaniq
            'yil': 2019,
            'narh': None,  # narhi belgilanmagan
            'km': 10325,
            'korobka': 'mexanika'
        }
        malibus.append(new_car)
for malibu in malibus:
    if malibu['rang']==None:
        malibu['rang']='Qizil'
for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=15000
    else: malibu['narh']=13200
for malibu in malibus:
    print(f" {malibu['model'].title()} rangi {malibu['rang'].title()} ishlab chiqarilgan yili {malibu['yil']} Narxi:{malibu['narh']} Yurgan yuli: {malibu['km']}  Karobka: {malibu['korobka'].title()}")
dasturlash={
    'ali':['python','java','c++'],
    'vali':['html', 'css','js'],
    'anvar':['php','sql'],
    'dlafruz':['photoshop','after effect']
}
for ism, tillar in dasturlash.items():
    print(f'{ism.title()} quyidagi dasturlash tillarini biladi: ')
    for til in tillar:
        print(til.upper())
for ism, tillar in dasturlash.items():
    print(f'{ism.title()} quyidagi dasturlash tillarini biladi:', end=' ')
    for til in tillar:
        print(til.upper(), end='')
    print("\n")


