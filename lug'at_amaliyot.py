# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:54:19 2024

@author: HP
"""
terminlar = {'boolean':'mantoqiy qiymat',\
             'float':"o'nlik son",\
            'for':'biror amalni qayta-qayta bajarish tsikli',\
           'if':'shartni tekshirish operatori',\
            'integer':'butun son'}
for key, value in sorted(terminlar.items()):
    print(f"{key} operatori {value} ma'nosini anglatadi")

davlatlar = {'uzbekistan':'toshkent',\
            'yoponiya':'tokio',\
            'xitoy':'pekin',\
            'indoneziya':'jakarta'}
for davlat in sorted(davlatlar.keys()):
         print(davlat.title())
for davlat in sorted(davlatlar.values()): 
    print(davlat.title())
davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? ").lower()
if davlat in davlatlar:
    print(f"{davlat.upper()}ning poytaxti {davlatlar[davlat].title()}")
else:
    print("kechirasiz,bizda bunday ma'lumot yo'q")
menu = {'osh':10000, 'shashlik':15000, 'somsa':7000, 'manti':5000, 'bifshteks':20000}
print("3 ta taom buyurtma qiling: ")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
    for buyurtma in buyurtmalar:
        if buyurtma in menu:
            print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
        else:
            print(f"Kechirasiz, bizda {buyurtma} yo'q")
    




