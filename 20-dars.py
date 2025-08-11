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

#def avto_info(kompaniya, model, rang, karobka, yil, narx=None):
#    avto={'kompaniya':kompaniya,
 #         'model':model,
#         'rang':rang,
#          'karobka':karobka,
#          'yil':yil,
#          'narx':narx}
#    return avto
#avto1=avto_info('GM', 'Tracker', 'qora', 'avtomat', '2025')
#vto2=avto_info('GM', 'Gentra', 'oq', 'mexanika', '2022', '13000')
#avtolar=[avto1, avto2]
#print('Onlayn bozordagi avtomashinalar: ')
#for avto in avtolar:
#    if avto['narx']:
#        narx=avto['narx']
#    else:
#        narx="No'malum"
#    print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")

#def oraliq(min,max,qadam=1):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        min+=qadam
#    return sonlar
#print(oraliq(1,11,2))

#def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
 #   avto = {'kompaniya':kompaniya,
 #           'model':model,
 #           'rang':rangi,
 #           'korobka':korobka,
 #           'yil':yili,
#            'narh':narhi}
#    return avto
#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
#avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting",end='')
#    kompaniya=input("Ishlab chiqaruvchi: ")
#    model=input("Modeli: ")
#    rangi=input("Rangi: ")
#    korobka=input("Korobka: ")
#    yili=input("Ishlab chiqarilgan yili: ")
#    narhi=input("Narhi: ")
#    
#    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#    
#    # Yana avto qo'shish-qo'shmaslikni so'raymiz
#    javob = input("Yana avto qo'shasizmi? (yes/no): ")
#    if javob=='no':
#        break
    
#def malumot(ism,familiya,t_yil,t_joy,tel_nomer=None,e_manzil=None):
#    talaba={'ism':ism,
#            'familiya':familiya,
#            "tug'ilgan yil":t_yil,
#            "tug'ilgan joy":t_joy,
#            "tel nomer":tel_nomer,
#            "email":e_manzil}
#    return talaba
#mijozlar=[]
#while True:
#    print("Quyidagi ma'lumotlarni kiriting")
#    ism=input("Mijoz ismi: ")
#    familiya=input("Mijoz familiyasi: ")
 #   t_yil=input("Tug'ilgan yili: ")
#    tel_nomer=input("Telefon raqami: ")
#    t_joy=input("email manzil: ")
#    mijozlar.append(malumot(ism, familiya, t_yil, t_joy,))
#    javob=input("Yana mijoz bormi? (yes/no)")
#    if javob=='no':
#        break
#print(mijozlar) 

#def sonlar(son_1,son_2,son_3):
#    if son_1>son_2>son_3:
#        print(son_1)
#    elif son_2>son_1>son_3:
#        print(son_2)
#    else:
#        print(son_3)
#sonlar(3, 5, 7)

def radius(rad,pi=3.14):
    malumot={'diametr':rad*2,
             'perimetr':2*pi*rad,
             'yuza':pi*rad**2}
    return malumot
radius(5)

























   