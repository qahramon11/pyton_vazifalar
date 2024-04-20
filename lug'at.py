# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:37:48 2024

@author: HP
"""

onam = {'ism':'zulayho', 't_yil':'1962', 't_vil': 'sirdaryo'}
#print(f"Onam {onam['ism'].title()} {onam['t_yil']}-yilda {onam['t_vil'].title()} viloyatida tug'ilgan")

ovqatlar = {
    'onam':'osh',
    'singlim':"lag'mon",
    'ukam':'manti'}
taom = ovqatlar['onam']
#print(f"Onamning sevimli taomi {taom}")

terminlar = {'string':'matn', 'float':"o'nlik soni", 'integer':'butun son', 'if':'agar'}
kalit = input("Kalit so'zinin kiriting: ").lower()  
#print(terminlar.get(kalit, 'Bunday so\'z mavjud emas'))


