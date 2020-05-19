liste = ["1","2","5a","10b","abc","10","50"]

# # #Liste elemanları içerisindeki sayısal değerleri bulunuz 


newListe = []
    
for i in liste : 
    try : 
        i=int(i)
        newListe.append(i)
    except ValueError:
        print('Sayısal değer değil')

    else :
        print(newListe)


#Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı verin

while True : 
    
    value = input('Lütfen bir sayı girin : ')
    if value == 'q' : 
        break
    try :
        value = int(value)
    except ValueError as ex: 
        print('sayısal bir değer değil')
        print(ex)
    else : 
        print(f"{value} sayıdır.")
    finally : 
        print('Validation tamamlandı.')
    
#Girilen parola içinde Türkçe karakter hatası verin 

import re

def checkPassword(psw):
    if re.search('[ışğüçö]',psw):
        raise TypeError('Parolanız TÜrkçe karakter içermemeli') 
    else:
        print('Geçerli parola')

try:
    password = input('Parola : ').lower()
    checkPassword(password)
except Exception as ex:
    print(ex)
else : 
    print('Geçerli parola : else')

finally : 
    print('Validation tamamlandı.')


# #Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verelim yollanan değer negatif ise veya int bir değer değil ise

def Faktoriyel(num):
    
    if num<0 : 
        raise Exception('Negatif sayılar ile faktöriyel hesaplanmaz.')
    if 0<=num <= 1 : 
        return 1
    else :
        return num * Faktoriyel(num-1)

try : 
    hesapla = int(input('faktöriyel hesaplaması için sayı giriniz :  '))
    result = Faktoriyel(hesapla)
except ValueError as ex : 
    print('sayısal bir değer giriniz')
else : 
    print(result)
finally: 
    print('Validation Tamamlandı .')
