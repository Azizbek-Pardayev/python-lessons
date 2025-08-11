# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 10:00:56 2025

@author: Azizbek
"""

#20-DARS Funksiyadan qiymat qaytarish

#def toliq_ism_yasa(ism, familiya):
#    """Toliq ism yaratuvchi"""
#    toliq_ism=f"{ism} {familiya}"
#    return toliq_ism
#talaba= toliq_ism_yasa("Olim", "Hakimov")
#print(talaba)

#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#    if otasining_ismi:
#        toliq_ism=(f"{ism} {familiya} {otasining_ismi}")
#    else:
#        toliq_ism=(f"{ism} {familiya}")
#    return toliq_ism.title()
#talaba=toliq_ism_yasa("olim", "hakimov")
#talaba1=toliq_ism_yasa("olim", "buriyev", "akbarovich")
#print(f"{talaba} va {talaba1} darsda yo'q")

def avto_info(kompaniya, model, rang, karobka, yil, narx=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rang,
          'karobka':karobka,
          'yil':yil,
          'narx':narx}
    return avto
avto1=avto_info('GM', 'Tracker', 'qora', 'avtomat', '2025')

print(avto1)










