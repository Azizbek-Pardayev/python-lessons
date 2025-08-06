# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 09:18:09 2025

@author: Azizbek
"""

#18-Dars While SIKLI, RO'YXATLAR VA LUG'ATLAR

#print("Yaqin do'stlar ro'yxatini tuzamiz.")
#ismlar=[]
#n=1 # ismlarni sanash uchu o'zgaruvchi
#while True:
#    savol=f"{n}-do'stingizni ismini kiriting:"
#    ism=input(savol)
#    ismlar.append(ism)
#    takrorlash=input("Yana ism qo'shasizmi. ha/yoq")
#    n+=1
#    if takrorlash !='ha':
#        break
#    
#print("Do'stlringiz ro'yxati:")
#for ism in ismlar:
#    print(ism.title())

#print("Do'stlar yoshini saqlaymiz.")
#dostlar={}
#ishora=True
#while ishora:
#    ism=input("Do'stlaringiz ismini kiriting:")
#    yosh=input(f"{ism.title()} ning yoshini kiriting:")
#    dostlar[ism]=int(yosh)
#    
#    javob=input("Yana ma'lumot qo'shasizmi.(ha/yoq)")
#    if javob =='yoq':
#        ishora=False 
#for ism, yosh in dostlar.items():
#    print(f"{ism} {yosh} yoshda")

#cars=['epica', 'gentra', 'tiko', 'tracker', 'tiko', 'nexia', 'tiko']
#car='tiko'
#while car in cars:
#    cars.remove(car)
#print(cars)

#talabalar=['olim','husan','hasan','tolib','umid']
#baholangan_talabalar={}
#while talabalar:
#    talaba=talabalar.pop()
#    baho=input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan_talabalar[talaba]=int(baho)
#print(baholangan_talabalar)

#print("Buyurtmalar ro'yxati: ")
#mahsulot=[]
#n=1
#while True:
#    buyurtma=input(f"{n}-buyurtmani kiriting: ")
#   mahsulot.append(buyurtma)
#    n+=1
#    javob=input("Yana buyurtma berasizmi.(ha/yoq)")
#    if javob=='yoq':
#        break
#print(mahsulot)

buyurtmalar=['cola','uzum','non','shirinlik']
mahsulotlar={'cola':14000,
             'olma':17000,
             'bulochka':7000,
             'shirinlik':30000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narx} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
        
