#Created on Tue Jun 17 08:43:28 2025
#@author: Azizbek


#print("hello world")
#5 ning 3-darajasini topish
#print(5**3)
#Sonning butun qismini olish uchun // belgidan foydalanamiz
#print(15//2)
#Gapni qatorlarga ajratish uchun """ """ va \n dan foydalanamiz
#print("""majburiy fanlarga 
#ona tili, tarix va matematika qo'shilgan""")
#print("majburiy fanlarga \nona tili, tarix va matematika qo'shilgan")
#bo'linmaning qoldig'ini topish uchun % belgisidan foydalanamiz
#print(15%4)
#print("Tomonlari 5 ga teng bo'lgan kvadrat yuzini top")
#print(5*5)
#ism='Azizbek'
#yosh=18
#print(ism)
#print(yosh)
#ism_sharif='Azizbek Pardaev'
#print(ism_sharif)

#O'zgaruvchi qilib belgilab bo'lmaydigan so'zlar
#False               class               from                or
#None                continue            global              pass
#True                def                 if                  raise
#and                 del                 import              return
#as                  elif                in                  try
#assert              else                is                  while
#async               except              lambda              with
#await               finally             nonlocal            yield
#break               for                 not
                 
#radius=2
#pi=3.14
#aylananing_uzunligi=2*pi*radius
#print('radiusi', radius, "bo'lgan", "aylananing uzunligi", aylananing_uzunligi)

#string(matn)

#matn="Men yangi 🚓 sotib oldim"
#print(matn)

#STRING USTIDA AMALLAR

#ism='Azizbek'
#print("Mening ismim "+ ism)
#ism='Azizbek'
#familiya='Pardaev'
#print(ism+familiya)
#print(ism+' '+familiya)

#f-string vazifasi

#ism='Azizbek'
#familiya='Pardaev'
#ism_sharif=f"{ism} {familiya}"
#print(ism_sharif)

#ism='james'
#familiya='bond'
#print(f"Mening ismim {ism}, familiyam {familiya}")

#Maxsus Belgilar
#\t so'z orasida katta joy qoldiradi
#\n qatorga ajratadi
#print('Hello \tworld')

#STRING METODLARI

#ism='james'
#familiya='bond'
#ism_sharif=f'{ism} {familiya}'
#print(ism_sharif.upper()) HAMMA HARFNI KATTA QILIB YOZIB BERADI
#print(ism_sharif.lower()) HAMMA HARFNI KICHIK QILIB YOZADI
#print(ism_sharif.title()) SO'ZLARNIG BOSH HARFLARINI KATTA YOZADI
#print(ism_sharif.capitalize()) BIRINCHI SO'ZNI 1-HARFINI KATTA BILAN YOZADI

#meva='    olmani    ' 
#print("Men "+meva.lstrip()+"yaxshi ko'raman") so'zning ortiqcha joyini qirqish
#print("men "+meva.rstrip()+" yaxshi ko'raman")
#print("men "+meva.strip()+" yaxshi ko'raman")

#INPUT

#ism=input("Ismingiz nima?\n") 
#print("Assalomu alaykum, "+ism.title())

# 6-DARS SONLAR

#radius = 24
#PI = 3.14 Katta harf bilan belgilansa o'zgarmas son
#diametr=2*radius
#print('Aylana uzunligi=',PI*diametr)

#ism = 'Azizbek'
#yosh = 18
#xabar = ism+' '+str(yosh)+' yoshda' #str() funksiya sonni o'zgartirmasdan 
#so'z turiga o'tkazib beradi. son + so'z mumkin emas
#print(xabar)

#t_yil=int(input("Tug'ilgan yilingizni kiriting: ")) #int so'zni songa o'girish 
#yosh= 2025-t_yil
#print("Siz ", yosh, " yoshdasiz")

#a=int(10)
#b=float(10)
#c=str(1212.21)
#print(a,b,c)

#son=int(input("Xohlagan son kiriting: "))
#kv= son**2
#print("Siz kiritgan sonning kvadrati ", kv)

#sav=int(input("Yoshingiz nechchida?\n>"))
#t_yil=2025-sav
#print("Siz", t_yil, "da tug'ilgansiz")

#a=float(input("Birinchi sonni kiriting:"))
#b=float(input("Ikkinchi sonni kiriting:"))
#print(f"{a}+{b}=",a+b)
#print(f"{a}-{b}=",a-b)
#print(f"{a}*{b}=",a*b)
#print(f"{a}/{b}=",a/b)

#7-dars List(Ro'yxat)

#mevalar = ['anor', 'olma', 'gilos', 'shaftoli']
#print(mevalar)
#print(mevalar[1])
#sonlar=[1,2,3,4,5,6]
#aralash=['bir', 'ikki', 'uch', 1,2,3]
#mevalar[0]='gilos'
#print(mevalar)
#mevalar.append('avacado') #listga yangi narsa qo'shish
#mevalar.insert(2, "banan") #listning ko'rsatilgan joyiga narsa qo'shish
#mevalar.remove('olma') #indeksini bilmasak o'chirsh usuli
#del mevalar[2] #listdan narsani olib tashlash
#mahsulot=mevalar.pop(3) #Listdan narsani yulib olish
#print('Men', mahsulot, 'sotib oldim', '\nOlinmagan mevalar: ', mevalar)

#dos=['Shoxrux', 'Diyor', 'Farruh', 'Abbos']
#jigar=dos.pop(0)
#bro=dos.pop()
#print('Salom, ',jigar,' bugun choyxona bormi?')
#print(bro,', bugun choyxonaga boramizmi?')

#8-dars Ro'yxatlar bilan ishlash
#Ro'yxatning qavsi [] bo'lishi kerak!!!!!
#cars=['mitsubiwi','mers','bmw', 'porche', 'volvo', 'chevrolet','toyota','audi']
#cars.sort() #Ro'yxatni alifbo tartibida joylashtiradi
#cars.sort(reverse=True) #Alifbo tartibiga teskari joylashtiradi
#print(cars) #Katta harf bilan kelsa doim boshidan yoziladi shuni to'g'irla
#print(sorted(cars)) #Ro'yxatga teginmagan holda tartiblaydi
#print(sorted(cars, reverse=True))
#cars.reverse() #Ro'yxatni teskari tartibda chiqaradi
#print(cars)
#print(len(cars)) #Ro'yxatdagi narsalar soni
#uzunligi=len(cars)
#sonlar=list(range(1,11))#Sonlar ro'yxatini chiqaradi(1 dan 10 ham kiradi 11 yoq)
#1 dan 30 gacha son kerak bolsa list(range(1,31)) 31ni kiritish kerak 
#toq_sonlar=list(range(1,20,2)) #toq sonlar ro''yxati
#print(toq_sonlar)
#juft_sonlar=list(range(0,20,2)) #oxiridagi 2 soni qadamni bildiradi
#print(juft_sonlar)
#max_qiymat=max(juft_sonlar) #Ro'yxatdagi maksimal qiymat
#print(max_qiymat)
#yigindi=sum(juft_sonlar)# ro'yxatdagi sonlar yig'indisi
#print(yigindi)
#print(cars[1:4]) #Ro'yxatdan kerakli joyini qirqib olish#
#my_cars=cars[:] #ro'yxatdan nusxa olish
#my_cars.remove('mitsubiwi') #my_cars ni o'zgartirsak ham cars o'zgarmaydi endi
#print(my_cars)

#TUPLE ro'yxat ya'ni o'zgartirib bo'lmaydigan ro'yxat
#toys=('mcqueen','teddy bear','train', 'bus', 'dino')
#toys.append('ciko') #metodlarni qo'llab bo'lmaydi
#print(toys)

#davlatlar=["O'zbekiston","Qozog'iston",'Germaniya','Amerika','Shvetsariya']
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
#davlatlar.reverse()
#davlatlar.sort(reverse=True)
#print(davlatlar)
#juft=list(range(120,1201,2))
#print(sum(juft))
#print(max(juft)-min(juft))
#print(len(juft))
#print(juft[:20], juft[261:281], juft[-20:])

#taomlar=['manti','xonim','somsa','shashlik','yaxni']
#nonushta=taomlar.copy()
#nonushta.remove('manti')
#nonushta.append('choy')
#print(taomlar)
#nonushta=tuple(nonushta)
#nonushta[0]='qaymoq va non'
#print(nonushta)
 
#9-dars FOR sikli

#mehmonlar=['Ali','Vali','shahi','Abbos', 'Farruh']
#for mehmon in mehmonlar:
 #   print('Salom', mehmon)
  #  print('Hayrli kun', mehmon)

#mehmonlar=['Ali','Vali','shahi','Abbos', 'Farruh']
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon} sizni 27-yanvar kuni nahorgi oshga taklif etamiz!")
#    print("Hurmat bilan Palonchiyevlar oilasi")

#sonlar=list(range(11,17))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2}ga teng")

#sonlar=list(range(11)) #1 dan 10 gacha sonlar ro'yxati
#sonlar_kvadrati=[] # bo'sh ro'yxat yaratib olamiz
#for son in sonlar: #sonlardagi har bir son uchun
#    sonlar_kvadrati.append(son**2) # kvadratini hisoblab olamiz
#print(sonlar)
#print(sonlar_kvadrati)    
    
#dostlar=[]
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
#print(dostlar)    

#mehmonlar=['Ali','Vali','shahi','Abbos', 'Farruh']
#for k in mehmonlar:
#    print("buqsan", k)

#sonlar=list(range(11,100,2))
#print(sonlar)
#for t in sonlar:
#    print(f"{t}ning kubi {t**3}")
#print(f"Kod {len(sonlar)} belgidan iborat edi.")

#kinolar=[]
#print("Eng yoqtirgan 5 ta kino nomi: ")
#for n in range(5):
#     kinolar.append(input(f"{n+1}-kino nomini kiriting:"))
#print(kinolar)

#suhbatdoshlar=[]
#raqam=int(input("Bugun nechta odam bilan gaplashding?"))
#for n in range(raqam):
#    suhbatdoshlar.append(input(f"{n+1}-odamning ismi: "))
#print(suhbatdoshlar)    

#10-dars if va else shartlari, tarmoqlanish

#avtolar=['audi','bmw','hundai','monza','tracker']
#if_agar_operatori 
#for avto in avtolar: #avtolar ichidan har bir avto uchun...
#    if avto=='bmw': #...agar avto 'bmw'ga teng bo'lsa
#        print(avto.upper()) #hamma harfini katta bilan yoz
#    else: #aks holda,...
#        print(avto.title()) # 1-harfini katta bilan yoz

#ism ='Ali'
#ism.lower() =='ali'
    
#  == tengmi degan shart
#  != teng emasmi sharti

#ism=input('Ismingizni kiriting: \n----') #ISMNI so'raymiz
#if ism.lower()!='azizbek': #tekshiramiz lower() bilan 
#    print('Uzr biz ', 'Azizbekni', 'kutyapmiz.') 
#else:
#    print('Salom, Azizbek')
    
#javob=float(input("12*6 ning javobini kiriting.>>>")) 
#if javob!=72:
#    print('JAvob xato!')

#yosh=int(input('Yoshingizni kiriting.>>>'))
#if yosh>=18:
#    print('Xush kelibsiz!')
#else:
#    print("Sur ivan!!!")
    
#login=input('Yangi login kiriting 5 harfdan kop bolsin: ')
#if len(login)<=5:
#    print("Login kamida 5 ta belgi bo'lsin")

#yosh=int(input("Yoshingizni kiriting: "))
#if yosh>65: print("Siz COVID-19 risk guruhiga kirasiz!!!")

#x,y=55,45
#print("x>y") if x>y else print('x<y')

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car=="gm":
#        print(car.upper())
#    else:
#        print(car.title())

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car!="gm":
#       print(car.title())
#    else:
#        print(car.upper())

#ism=input("Ismingizni kiriting: ")
#if ism.lower()=="azizbek":
#    print("Xush kelibsiz, Admin!")
#else:
#    print("Xush kelibsiz, ",ism)    

#son=float(input("1-sonni kiriting:>>>"))
#son_2=float(input("2-sonni kiriting:>>>"))
#if son==son_2:
#    print("Sonlar teng")

#son=float(input("Son kiriting: "))
#if son<0:
#    print("Manfiy son")
#else:
#    print("Musbat son")    

#son=float(input("Son kiriting: "))
#if son>=0:
#    print(son**(1/2))
#else:
#    print("Musbat son yoz buq")

#11-dars if-else-elif

#yosh=int(input("Yoshingiz nechchida? "))
#if yosh<=5:
#    narx=0
#elif yosh<=12:
#    narx=5000
#elif yosh<=18:
#    narx=8000
#else:
#    narx=10000
#print(f"Siz kirish uchun {narx}  so'm to'lashingiz kerak")
    
#kun=input('Bugun nima kun? ')
#if kun.lower()=='yakshanba' or kun.lower()=='shanba':
#    print('Bugun dam olish kuni.')
#else:
#    print('Bugun ish kuni')

#kun=input('Bugun nima kun? ')
#harorat=float(input("Havo harorati qanday? "))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Toqqa gooooooooo")
#elif kun.lower()=='yakshanba' and harorat<=30:
#    print("Uyda uxlaymiz")

#BOOLEAN ma'lumot turi

#narx=15000
#choy=True
#salat=True
#if choy and salat:
#    narx=narx+10000
#elif choy or salat:
#    narx=narx+5000
#print(f"Siz {narx} so'm to'laysiz")

#narx=15000
#choy=1 # 1=True
#non=1
#salat=0 #0=False
#shirinlik=1
#suv=1
#if choy:
#    narx=narx=2000
#    print("Mijoz choy sotib oldi")
#if non:
#    narx=narx+5000
#    print("Mijoz non sotib oldi")
#if salat:
#    narx=narx+15000
#    print("Mijoz salat sotib oldi")
#if shirinlik:
#    narx=narx+20000
#    print('Mijoz shirinlik sotib oldi')
#if suv:
#    narx=narx+14000
#    print('Mijoz suv sotib oldi')
#print(f"Jami summa: {narx}")

#in operatori

#menu=['shashlik','norin','manti','osh','somsa','tandir']
#taom=input("Qaysi ovqatni yeysiz? ")
#if taom.lower() in menu:
#    print("Buyurtmangiz qabul qilindi")
#else:
#    print("Bizda bunday ovqat yo'q")

#menu=['shashlik','norin','manti','osh','somsa','tandir']
#buyurtmalar=['shashlik','tandir','osh','lavash']
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz menuda {taom} yo'q")
#else:
#    print("Savatingiz bo'sh")

#yosh=int(input("Yoshingizni kiriting: "))
#if yosh>=60 or yosh<=6:
#    narx=0
#elif yosh<=18:
#    narx=10000
#else:
#    narx=20000
#print(f"Siz {narx}  so'm to'lov qilasiz")

#son1=float(input("1-sonni kiriting: "))
#son2=float(input("2-sonni kiriting: "))    
#if son1>son2:
#    print(f"{son1}>{son2}")
#elif son1<son2:
#    print(f"{son2}>{son1}")
#else:
#    print(f"{son1}={son2}")

#mahsulot=['olma','gilos','sabzi','nok','anjir','shaftoli','tarvuz','qovun']
#savat=[]
#print("5 ta meva kiriting: ")
#for n in range(5):
#    savat.append(input(f"{n+1}-meva nomini kiriting: "))

#if savat:
#    for meva in savat:
#        if meva in mahsulot:
#        else:
#            print(f"Do'konimizda {meva} yo'q")
#else:
#    print("Savat bo'sh")

#son=float(input("Juft son kiriting: "))
#if son%2:
#    print("Bu juft son emas")
#else:
#    print("Rahmat")

#mahsulot=['olma','gilos','sabzi','nok','anjir','shaftoli','tarvuz','qovun']
#savat=[]
#print("5 ta meva kiriting: ")
#for n in range(5):
#    savat.append(input(f"{n+1}-meva nomini kiriting: "))
##    
#bor_mahsulotlar=[]
#mavjud_emas=[]
#for meva in savat:
#        if meva in mahsulot:
#            bor_mahsulotlar.append(meva)
#        else:
#            mavjud_emas.append(meva)
#if mavjud_emas:
#    print("Do'konimizda bu mahsulotlar yo'q: ")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#else:
#    print("Siz so'ragan barcha mahsulot do'konda bor")

#son=int(input("Istalgan butun son kiriting: "))
#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

#12-dars xatolar

#son = float(input("Juft son kiriting: "))
#if son%2!=0:
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")

#yosh = int(input("Yoshingiz nechida?"))

#if yosh<=4 or yosh>=60:
#    narh = 0
#elif yosh < 18:
#    narh = 10000
#else:
#    narh = 20000
#print(f"Chipta {narh} so'm")

#x = float(input("Birinchi sonni kiriting: "))
#y = float(input("Ikkinchi sonni kiriting: "))
#if x==y:
#    print(f"{x}={y}")
#elif x<y:
#    print(f"{x}<{y}")
#else:
#    print(f"{x}>{y}")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat=[]

#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if mahsulotlar:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            print(f"Do'konimizda {mahsulot} bor")
#        else:
#            print(f"Do'konimizda {mahsulot} yo'q")
#else: 
#    print("Savatingiz bo'sh")

#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)

#if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q:")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
#users = ['alisher1983','aziza','yasina' 'umar']

#login = input("Yangi login tanlang: ")

#if login.lower() in users:
#    print('Login band, yangi login tanlang!')
#else:
#    print("Xush kelibsiz!")










