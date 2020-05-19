
def not_gir():
    ad = input('isim : ')
    soyad = input('Soyisim : ')
    not1 = input('not 1 : ')
    not2 = input('not 2 : ')
    not3 = input('not 3 : ')

    with open("notlar.txt","a",encoding="utf-8") as file : 
        
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n" )

def hesapla(satir) : 
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciBilgisi = liste[0]

    notlar = liste[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama= (not1 + not2 + not3 )/3
    
    if ortalama >=90 and ortalama <=100 : 
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89 : 
        harf = "BA"
    elif ortalama >= 80 and ortalama <= 84 : 
        harf = "BB"
    elif ortalama >= 75 and ortalama <= 79 : 
        harf = "CB"
    elif ortalama >= 70 and ortalama <= 74 : 
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69 : 
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64 : 
        harf = "DD"
    elif ortalama >= 50 and ortalama <= 59 : 
        harf = "FD"
    else :
        harf = "FF"

    return ogrenciBilgisi + " : " + harf +"\n"

def notlari_oku() : 

    with open("notlar.txt","r",encoding="utf-8" ) as file : 

        for i in file: 
            print(hesapla(i))

def not_kayit_et() : 
    with open("notlar.txt","r",encoding="utf-8") as file : 
        liste = []
        for i in file :
            liste.append(hesapla(i))

        with open("ortalama.txt","w",encoding= "utf-8") as ort : 
            for i in liste :
                ort.write(i)


while True :
    islem = input('\n1 - Notları Oku\n2 - Not Gir\n3 - Not Kayıt Et \nişlem : ')

    if islem == "1" : 
        notlari_oku()

    elif islem =="2" : 
        not_gir()

    elif islem == "3" :
        not_kayit_et()

    else :
        break