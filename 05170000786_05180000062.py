liste=[]
ic_ice_liste=[] #Başlangıçta gösterilen orjinal liste
degisen_liste=[] # Dolu boş ve normal içeren kullanıcının değiştirdiği ve sadece kullanıcıya gözüken liste
degisen_liste2=[] # degisen listedeki kesin doluların normale çevrilip karşılaştırıldığı liste
satir=0
string=""
kontrol=[]
bitis1=[]

zorluk_derecesi=str(input("Lütfen zorluk derecesi giriniz. Çok kolay oyun=cko, kolay oyun=ko,orta oyun=oo,zor oyun=zo,çok zor oyun=czo:")) #Satır ve sutunların kaç olacağını belirler.
while zorluk_derecesi not in ["cko","ko","oo","zo","czo"]:
    zorluk_derecesi=str(input("Lütfen zorluk derecesi giriniz. Çok kolay oyun=cko, kolay oyun=ko,orta oyun=oo,zor oyun=zo,çok zor oyun=czo:"))
try:
    if zorluk_derecesi=="cko":
        satir_sutun=3
        dosya=open("ornek_oyunlar/cok_kolay_oyun/hitori_bulmaca.txt", "r")
    elif zorluk_derecesi=="ko":
        satir_sutun=5
        dosya=open("ornek_oyunlar/kolay_oyun/hitori_bulmaca.txt", "r")
    elif zorluk_derecesi=="oo":
        satir_sutun=6
        dosya=open("ornek_oyunlar/orta_oyun/hitori_bulmaca.txt", "r")
    elif zorluk_derecesi=="zo":
        satir_sutun=8
        dosya=open("ornek_oyunlar/zor_oyun/hitori_bulmaca.txt", "r")
    elif zorluk_derecesi=="czo":
        satir_sutun=9
        dosya=open("ornek_oyunlar/cok_zor_oyun/hitori_bulmaca.txt", "r")
except FileNotFoundError:
    print("Dosya Bulunamadı")
else:
    for i in range(1,satir_sutun+1):
        satir=dosya.readline()
        liste.append(satir)
    for j in range(0,len(liste)):
        a=liste[j].split( )
        ic_ice_liste.append(a)
        b=liste[j].split( )
        degisen_liste.append(b)
        c=liste[j].split( )
        degisen_liste2.append(c)

def son_hali_goster(): # Her işlem sonrası çıkan listeyi gösterir.
    def sutun_goster(satir_sutun):
        for i in range(1,satir_sutun+1):
            print(" ",i,end="")
    sutun_goster(satir_sutun)
    print()  # end düzeltildi
    for i in range(satir_sutun):  # başlangıcı gösteren bölüm
        string1 ='--'.join(degisen_liste[i])
        print(i+1,string1)

def sutun_goster(satir_sutun):
    for i in range(1,satir_sutun+1):
        print(" ",i,end="")

def islem_al():        #Bu fonksiyon kullanıcıdan işlem hamlelerini sağlıklı bir şekilde almaya yarar.
    global islem_list
    islem=input("Satır numarasını (1-3), sütun numarasını (1-3) ve işlem kodunu (B:boş, D:dolu, N:normal/işaretsiz) aralarında boşluk bırakarak giriniz:")
    islem_list=islem.split()
    for j in range(1,satir_sutun+1):
        kontrol.append(j)
    #islem_list[] içindekiler str konrol içi int dir.

    for i in range(2):
        while int(islem_list[i]) not in kontrol:
            print("HATA. Geçersiz bir komut girdiiniz. Tekrarlayınız.")
            islem_al()
    while str(islem_list[2]) not in ["B","D","N","b","d","n"]:
        print("HATA. Geçersiz bir komut girdiiniz. Tekrarlayınız.")
        islem_al()

def oyun_bitis_2_3(): #Aynı satır veya sutunda aynı elemanlar olup olmadığını kontrol eder. bitis2 yataylara, bitis3 dikeylere bakar
    global bitis2
    global bitis3
    sutun_listesi = []
    for i in range(satir_sutun):
        a = []
        for j in range(satir_sutun):
            a.append(degisen_liste2[j][i])
        sutun_listesi.append(a)

    class BreakIt(Exception): pass
    try:
        for i in range(satir_sutun):
            for j in range(satir_sutun):
                if degisen_liste2[i][j]!="X":
                    h=degisen_liste2[i][j]
                    del degisen_liste2[i][j]
                    if h in degisen_liste2[i]:
                        bitis2 = "Olmadı"
                        degisen_liste2[i].insert(j, h)
                        raise BreakIt
                    else:
                        bitis2="Durum sağlandı"   #Bu durum olursa oyun biter. Aynı satırda 2 eleman yoktur demek.
                        degisen_liste2[i].insert(j,h)
    except BreakIt:
        pass
    try:
        for i in range(satir_sutun):
            for j in range(satir_sutun):
                if sutun_listesi[i][j] != "X":
                    g = sutun_listesi[i][j]
                    del sutun_listesi[i][j]
                    if g in sutun_listesi[i]:
                        bitis3 = "Olmadı"
                        sutun_listesi[i].insert(j, g)
                        raise BreakIt
                    else:
                        bitis3 = "Durum sağlandı"
                        sutun_listesi[i].insert(j, g)
    except BreakIt:
        pass

def dolu_bir_nokta(): # Herhangi bir dolu nokta döndürür.
    for i in range(satir_sutun):
        for j in range(satir_sutun):
            if degisen_liste2[i][j]!="X":
                kontrol1.append([[i],[j]])
                return i,j

def alt_ust_sag_sol(i,j):
    global kontrol1
    s=satir_sutun-1
    if (i<=s and j + 1 <=s) and (i>=0 and j+1>=0):
        if degisen_liste2[i][j+1] != "X":
            if not [[i],[j+1]] in kontrol1:
                kontrol1.append([[i], [j+1]])

    if (i<=s and j-1<=s) and (i>=0 and j-1>=0):
        if degisen_liste2[i][j-1] != "X":
            if not [[i], [j-1]] in kontrol1:
                kontrol1.append([[i], [j-1]])

    if (i+1<= s and j <= s) and (i+1>=0 and j>=0):
        if degisen_liste2[i+1][j] != "X":
            if not [[i+1], [j]] in kontrol1:
                kontrol1.append([[i+1],[j]])

    if (i-1<= s and j<= s) and (i-1>=0 and j>=0):
        if degisen_liste2[i-1][j] != "X":
            if not [[i-1],[j]] in kontrol1:
                kontrol1.append([[i-1],[j]])

def oyun_bitis_4(): # Dolu kısımların birbiriyle bağlantılarının kontrol edildiği bölümdür.
    global bitis4
    global kontrol1
    kontrol1=[]
    kontrol2=[]

    i_ve_j=dolu_bir_nokta()
    i=i_ve_j[0]
    j=i_ve_j[1]
    alt_ust_sag_sol(i,j)

    for elli in range(50):
        for k in kontrol1: # bir eleman mesela [[[1],[3]],...]
            i=k[0][0]
            j=k[1][0]
            alt_ust_sag_sol(i,j)

    for i in range(satir_sutun):
        for j in range(satir_sutun):
            if degisen_liste2[i][j]!="X":
                kontrol2.append([[i],[j]])

    kontrol1=sorted(kontrol1)
    if kontrol1==kontrol2:
        bitis4=True
    else:
        bitis4=False

son_hali_goster() #Oyun başlangıcını gösterir.
while True:
    bitis2=""
    bitis3=""
    islem_al()

    a=int(islem_list[0])-1  # Bu kısım kullanıcının sayıları değiştirmesini sağlar
    b=int(islem_list[1])-1
    c=islem_list[2]
    if c=="B" or c=="b":
        degisen_liste[a][b]="X"
        degisen_liste2[a][b]="X"
    elif c=="D" or c=="d":
        degisen_liste[a][b] = str("(" + ic_ice_liste[a][b] + ")")
    elif c=="N" or c=="n":
        degisen_liste[a][b] = str(ic_ice_liste[a][b])
        degisen_liste2[a][b]=str(ic_ice_liste[a][b])

    for i in range(satir_sutun-1):
        for j in range(satir_sutun-1):
            if (degisen_liste[i][j]=="X" and degisen_liste[i][j+1]=="X") or (degisen_liste[j][i]=="X" and degisen_liste[j+1][i]=="X") :
                print("Hata! Boş kareler, yatay ya da dikey olarak birbirlerine komşu olamazlar")
                bitis1.append(1)
            else:
                bitis1.append(0)
    for i in range(satir_sutun-1):
        for j in range(satir_sutun-1):
            if not (degisen_liste[i][j]=="X" and degisen_liste[i][j+1]=="X") or (degisen_liste[j][i]=="X" and degisen_liste[j+1][i]=="X"):
                for i in bitis1:
                    if i==1:
                        del bitis1[i]

    oyun_bitis_2_3()
    oyun_bitis_4()
    son_hali_goster()

    if bitis1!=1 and (bitis2=="Durum sağlandı" and bitis3=="Durum sağlandı"):
        if bitis4==True:
            print("Tebrikler! Kazandınız.")
            break

dosya.close()