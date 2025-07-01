#15-dars Lug'at elementlari bilan ishlash

#talaba_0={'ism':'ali',
#          'familiya':'shamsiyev',
#          'yosh':'21',
#          'kurs':'4'}
#print(talaba_0.items())  #items metodi lug'atdagi lug'atlarni chiqarib beradi
#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat}\n")

#telefonlar={'shoxrux':'samsung s10e',
#            'diyorbek':'samsung s20+',
#            'farruh':'redmi 8',
#            'azizbek':'redmi 6'}
#for key, value in telefonlar.items():
#    print(f"{key.title()}ning telefoni {value}")

#mahsulotlar={'olma':'10000',
#             'anor':'15000',
#             'uzum':'12000',
#             'shaftoli':'8000'}
#print(mahsulotlar.keys())

#print("Do'konimizdagi mahsulotlar: ")
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())

#print("Do'konimizdagi mahsulotlar: ")
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())

#bozorlik=['olma', 'kartoshka', 'anor', 'piyoz']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm'")
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos do'koningizga {buyum} ham olib keling.")

#print("Do'konimizdagi mahsulotlar: ")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())

# # values
#print("Mahsulotlar narxlari: ")
#for narx in mahsulotlar.values():
#    print(narx)

# # set
#mahsulotlar={'olma':'10000',
#             'anor':'15000',
#             'uzum':'12000',
#             'shaftoli':'8000',
#             'non':'8000',
#             'kartoshka':'10000',
#             'anjir':'11000',
#             'tuxum':'15000'}
#print("Mahsulotlar narxlari: ")
#for narx in set(mahsulotlar.values()):
#    print(narx)

#toys = {'car','bear', 'ball', 'lamp','ball', 'bear'}
#print(toys)

#python={'tuple':"o'zgarmas ro'yxat",
#        'sort':'ro\'yxatni alifbo tartibida qiladi',
#        'key':'lug\'atdagi kalitlar',
#        'set':'takrorlanmas ro\'xat',
#        'value':'qiymat',
#        'integer':'butun son',
#        'float':'o\'nlik son',
#        'list':'ro\'yxat'}
#for kalit,qiymat in sorted(python.items()):
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat}")

#dav_poy={'o\'zbekiston':'toshkent',
#         'qozog\'iston':'shimkent',
#         'germaniya':'berlin',
#         'aqsh':'washington',
#         'korea':'seul'}
#print("Quyidagi davlatlar: ")
#for davlat in dav_poy.keys():
#    print(davlat.title())
#print('Quyidagilar poytaxtlari: ')
#for poy in dav_poy.values():
#    print(poy.title())

#dav_poy={"o'zbekiston":'toshkent',
#         "qozog'iston":'shimkent',
#         'germaniya':'berlin',
#         'aqsh':'washington',
#         'korea':'seul'}
#nom=input("Davlat nomini kiriting: ").lower()
#poytaxt=dav_poy.get(nom)
#if poytaxt==None:
#    print("Bizda bu davlat haqida ma'lumot yo'q.")
#else:
#    print(f"{nom.upper()}ning poytaxti {poytaxt.title()}")
#mahsulotlar={'olma':'10000',
#             'anor':'15000',
#             'uzum':'12000',
#             'shaftoli':'8000',
#             'non':'8000',
#            'kartoshka':'10000',
#             'anjir':'11000',
#             'tuxum':'15000'}
#buyurtmalar=[]
#print("3 ta buyurtma kiriting:")
#for n in range(3):
#    buyurtmalar.append(input(f"{n+1}-buyurtma nomi: ").lower())
#    
#for buyurtma in buyurtmalar:
#    if buyurtma in mahsulotlar:
#            print(f"{buyurtma.title()} {mahsulotlar[buyurtma]} so'm")
#    else:
#        print(f"Kechirasiz bizda {buyurtma} yo'q")
