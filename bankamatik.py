from random import randint
from datetime import datetime,date

musteri = {1:{'ad':'admin','soyad':'admin','tc':'0000','dogum_tarihi':'1999/20/11','sehir':'izmir','adres':'konak','parola':'admin123','bakiye':5000,'ekhesap':1000}}
hesap_no=1012 #Bankaya kayıt olurken kullanılan hesap no

def hesap_kayit(name,surname,tc_no,dogum_tarihi,sehir,adres,parola,bakiye=0,ekhesap=500): #kayıt parametrelerini alıp musteri sözlüğünde hesap nosuyla
    global hesap_no                                     #hesap_no:{bilgiler} ile sözlük bağlantısı yapan fonksiyon


    musteri[hesap_no]={'ad':name,'soyad':surname,'tc':tc_no,'dogum_tarihi':dogum_tarihi,'sehir':sehir,'adres':adres,'parola':parola,'bakiye':bakiye,'ekhesap':ekhesap}
    
    print('*'*50)
    print('HESAP  BİLGİLERİNİZ : ')
    print(f'Hesap no : {hesap_no}*  \nİsim : {name}* \nSoyisim : {surname}* \nTC Kimlik No : {tc_no}* \nDoğum Tarihi : {dogum_tarihi}* \nŞehir : {sehir}* \nAdres : {adres}* \nParola : {parola}')
    print('PAROLANIZI KİMSEYLE PAYLAŞMAYIN !')
    #kayıt işlemi gerçekleştikten sonra kişisel bilgilerini ekrana basar

def hesap_para_cekme(hesap_no,tutar):
    #Bakiyeye göre hesaptan para çekme ve ek hesap kullanımı
    if musteri[hesap_no]['bakiye'] >= tutar :   #musterinin bakiyesi çekmek istediği tutardan büüyük mü diye kontrol eder

        musteri[hesap_no]['bakiye']-=tutar      #çekmek istediği tutar musterinin bakiyesinden çıkarılır

        hesap_bakiye = musteri[hesap_no]['bakiye']  
        
        print(f'Kalan bakiyeniz {hesap_bakiye} \nİYİ GÜNLERDE HARCAMANIZ DİLEĞİ İLE...')    #yeni bakiyesi ekrana bastırırlır
        
        print('*'*75)
    
    else : #eğer musterinin bakiyesi tutarı çekmeye yetmiyorsa
        
        if musteri[hesap_no]['bakiye']+musteri[hesap_no]['ekhesap']>=tutar :  #mmusterinin bakiyesi ile ek hesap bakiyesi toplanır ve eğer 
                                                                            #çekmek istediği tutara eşit ve ya büyük olursa 
            ekhesap_kullanim = input('ek hesap kullanılsın mı ? (e/h) : ')  #ek hesaptan para kullanmak isteyip istemediğinin sorar
            
            if ekhesap_kullanim == 'e':             # Kullanmak isterse 
                
                ekhesap_kullanim_miktari = tutar  - musteri[hesap_no]['bakiye'] #musterinin hesap bakiyesi sıfırlanır ve tutar da ek hesapta ki
                musteri[hesap_no]['bakiye']=0                                   # bakiyeden çıkarılır ek hesaptan kullanım miktarı belirlendikten sonra
                musteri[hesap_no]['ekhesap']-=ekhesap_kullanim_miktari

                hesap_ek_hesap=musteri[hesap_no]['ekhesap']

                print(f'Ek hesap kalan bakiyeniz {hesap_ek_hesap} \nİYİ GÜNLERDE HARCAMANIZ DİLEĞİ İLE...')
                    #ek hesapta kalan bakiyesi ekrana bastırılır
                print('*'*75)
            
            else :
                
                print(f'Hesap bakiyeniz : {hesap_bakiye}')
                #   eğer ek hesaptan para kullanmayı red ederse ekrana hesap bakiyesi basılır
                print('*'*75)
        
        else :
            
            print('Bakiyeniz yetersizdir !')
                        #eğer müşterinin bakiyesi ve ek hesap bakiyesi toplamı çekeceği tutarı karşılayamazsa ekrana bastırılır
            print('*'*75)

def hesap_bakiye_yatırma(hesap_no,tutar):


    if musteri[hesap_no]['ekhesap']<500 :   #hesaba para yatırılırken ek hesap limiti kontrol edilir eğer ek hesaptan para kullanıldıysa borcu vardır
        
        borc = 500 - musteri[hesap_no]['ekhesap']    #Borcu hesaplanır ek hesap limiti(500)
      
        if tutar >= borc :  #yatırdığı tutar borcundan fazla ise
           
            musteri[hesap_no]['ekhesap'] += borc    #ek hesaba borç eklenir ve ek hesap (500)limitine ulaşır
            
            tutar = tutar-borc          #Yatırılan tutardan da borç çıkarılır ve yeni tutar oluşturulur

    musteri[hesap_no]['bakiye']+=tutar  #kalan tutar  yatırılır borcu yoksa yatırdığı tutar eklenir

    bakiye=musteri[hesap_no]['bakiye']

    ekhesap_bakiye=musteri[hesap_no]['ekhesap']

    print(f'Yeni hesap bakiyeniz : {bakiye} \nEk Hesap Bakiyeniz : {ekhesap_bakiye} \nYatırdığınız tutar : {tutar}')
            #yeni hesap bakiyeleri ekrana bastırılır
    print('*'*75)


def bakiye_aktarma(hesap_no,havale_hesap_no,tutar): #Bakiye aktarma
    
    if musteri[hesap_no]['bakiye'] >= tutar:    #müşterinin hesap bakiyesi kontrol edilir ve göndermek istediği tutardan fazla bakiyesi varmı diye bakılır
        
        musteri[hesap_no]['bakiye']-=tutar          #Göndermek istediği tutar müşterinin bakiyesinden çıkkarılır
               
        bakiye = musteri[hesap_no]['bakiye']

        if musteri[havale_hesap_no]['ekhesap']<500 :        #paranın aktarıldığı kişinin borcu var mı kontrol ediliyor eğer var ise

            borc = 500 - musteri[havale_hesap_no]['ekhesap']    #paranın gönderildiği kişinin borcu hespalanıyor

            if tutar >= borc :                                  #Gönderilen tutar borcundan büyük ise

                musteri[havale_hesap_no]['ekhesap'] += borc     #Havalenin gittiği kişinin borcu kapanıyor

                tutar = tutar-borc                              #kalan tutar hesaplanıyor
        
        musteri[havale_hesap_no]['bakiye']+=tutar   #gönderilecek kişinin hesap nosuna göre kişinin hesabına eklenir bakiye

        print(f'Hesap bakiyeniz  : {bakiye} \nGönderilen hesap no : {havale_hesap_no} \n Gönderilen tutar : {tutar}')
                        #yeni hesap bakiyesi gönderdiği tutar ve gönderdiği kişinin hesap nosu ekrana basılır
        print('*'*75)

    else :

        if musteri[hesap_no]['bakiye'] + musteri[hesap_no]['ekhesap']>=tutar : #müşterinin ek hesap ve bakiyesi toplanarak göndereceği tutardan büyük
                                                                                #mü kontrol edilir
            onay = input('Yeterli bakiyeniz yok , Ek hesap kullanılsın mı (e/h) : ')
                                                            #ek hesap bakiyesini kullanmak isteyip istemediği sorulur
            print('*'*75)
            
            if onay=='e':
                                        #kullanmak istiyorsa
                ek_hesap_tutar = tutar - musteri[hesap_no]['bakiye'] #ek hesaptan kullanılacak tutar hesaplanır

                musteri[hesap_no]['bakiye']=0                           #bakiye sıfırlanır

                musteri[hesap_no]['ekhesap']-=ek_hesap_tutar                #ek hesap bakiyesinden kullanılacak tutar çıkarılır

                if musteri[havale_hesap_no]['ekhesap']<500 :        #paranın aktarıldığı kişinin borcu var mı kontrol ediliyor eğer var ise

                    borc = 500 - musteri[havale_hesap_no]['ekhesap']    #paranın gönderildiği kişinin borcu hespalanıyor

                    if tutar >= borc :                                  #Gönderilen tutar borcundan büyük ise

                        musteri[havale_hesap_no]['ekhesap'] += borc     #Havalenin gittiği kişinin borcu kapanıyor

                        tutar = tutar-borc                              #kalan tutar hesaplanıyor

                musteri[havale_hesap_no]['bakiye']+=tutar               #tutar gönderdiği kişinin bakiyesine eklenir

                bakiye = musteri[hesap_no]['bakiye']            
                
                ek_hesap_bakiye = musteri[hesap_no]['ekhesap']

                print(f'Hesap bakiyeniz  : {bakiye} \nEk hesap bakiye : {ek_hesap_bakiye} \nGönderilen hesap no : {havale_hesap_no} \nGönderilen tutar : {tutar}')
                        #yeni bakiye bilgileri gönderdiği tutar ve gönderdiği kişinin hesap nosu ekrana basılır
                print('*'*75)
            else :

                print(f'Hesap bakiyeniz : {hesap_bakiye}')#ek hesap kullanmak istemezse ekrana basılır
               
                print('*'*75)
        else : 

            print('Bakiyeniz yetersizdir !')#ek hesap ve bakiyesi yetersiz ise ekrana basılır
           
            print('*'*75)

while True :    #Program başlar
    
    print('*'*75)
    
    islem=input('Yapmak istediğiniz işlem için numarasını yazın  \n1-Hesap Kayıt \n2-Hesap Giriş \n3-Kapat \nİşleminiz : ')
                    #Yapılmak istenen işlemin numarası girilir
    print('*'*75)
    
    if islem == '1' :
                        #Hesap kayıt işlemi
        print('*'*75)
        
        print('Lütfen aşağıdaki istenen bilgileri eksiksiz doldurunuz.')
        
        print('*'*75)
        
        date1=datetime.now()            #şuan ki tarih bilgisi alınır

        ad = input('İsim : ')           #isim girdisi
        soyisim = input('Soyisim : ')   #soyisim girdisi
        tc_no = input('Tc Kimlik No : ')    #tc kimlik girdisi
        dogum_tarihi = input('Doğum Tarihi (yy/aa/gg) : ')  #doğum tarihi girdisi
        sehir = input('Şehir : ')               #şehir girdisi
        adres = input('Adres : ')               #adres girdisi
        parola = input('Parola : ')             #parola girdisi

        dogum_tarihi=dogum_tarihi.split('/')    #girilen tarih split methodu ile "/" belirlenen yerlerden parçalanır liste haline getirilir
        
        yas_hesap = date(year=int(dogum_tarihi[0]),month=int(dogum_tarihi[1]),day=int(dogum_tarihi[2])) #yaş hesaplaması için tarihe çevrilir
        
        day = (date1.date() - yas_hesap).days           #şuan ki zaman ile kişinin doğum tarihi arasındakii gün sayısı hesaplanır
        
        dogum_tarihi = '/'.join(dogum_tarihi)           #listeye çevrilen doğum tarihi bilgisi yeniden string ifadeye döner

        if day > 365*18 :       #yukarıda hesaplanan gün bilgisi 18 yaşından büyük mü diye kontorl edilir
            
            hesap_no+=2         #hesap numaraları kayıt edilirken aynı olmaması için her girdide 2 artar
           
            onay = input('İşleminizi onaylıyormusunuz (e/h) : ')    #kaydı onaylıyor mu 
            
            print('*'*75)
           
            if onay == 'e' :        #kayıt onaylandı ise hesap_kayit fonksiyonuna bilgiler gönderilir bakiye ve ek hesap bilgisi gönderilmez
                                    # onlar varsayılan değer olarak ayarlanmıştır
                hesap_kayit(ad,soyisim,tc_no,dogum_tarihi,sehir,adres,parola)
                
                input('Hesabınız açılmıştır İYİ GÜNLER DİLERİZ... \nMenüye dönmek için bir tuşa basınız : ')
                
                print('*'*75)
            
            elif onay == 'h' : 
                
                input('Hesap kayıt işleminiz tarafınızca iptal edilmiştir İYİ GÜNLER... \nMenüye dönmek için bir tuşa basınız : ')
                            #kayıt işlemi iptal edilirse ekrana basılır
                print('*'*75)
            
            else : 
                
                print('Hatalı tuşlama yaptınız.')
                
                print('*'*75)
        
        else : 
            
            input('Üzgünüz henüz banka hesabı açabilecek yaşta değilsiniz. \nMenüye dönmek için bir tuşa basınız : ')
                                #doğum tarihinden hesaplanan gün sayısı 18*365 i geçmemişse bu mesaj bastırılır
            print('*'*75)
    
    if islem == '2' :       #Hesap giriş
       
        hesap_no_giris = int(input('Hesap No : '))

        hesap_parola_giris = input('Parola : ')
        
        print('*'*75)
       
        if musteri[hesap_no_giris]['parola'] == hesap_parola_giris :    #musteri sözlüğünden alınan inputlardaki değerler hesap_nonun içindeki parolayı kontrol eder

            while True : #hesap girişinden sonra kişi istediği kadar işlem yapabilmesi için 

               
                musteri_ad=musteri[hesap_no_giris]['ad']
               
                print(f'Hoşgeldiniz Sayın {musteri_ad}.\n') #Giriş yapan müşterinin adı basılır
                
                hesap_bakiye = musteri[hesap_no_giris]['bakiye']
               
                hesap_ek_hesap = musteri[hesap_no_giris]['ekhesap']
                    
                print(f'Hesap bakiyeniz : {hesap_bakiye}')  #Müşterinin bakiyesi ve ek hesap bilgisi bastırılır
               
                print(f'EK hesap bakiyeniz : {hesap_ek_hesap} \n\n')

                giris_islem = input('İŞLEMLER : \n1-Para Çekme \n2-Para Yatırma \n3-Para Gönderme  \n5-Çıkış \nİşleminiz : ')
                                            #Müşteriye yapmak istediği işlemleri sorar ve girdiye göre işlemler çalışır
                print('*'*50)
               
                if giris_islem =='1' :          #Para çekme
                
                    hesap_bakiye = musteri[hesap_no_giris]['bakiye']
                    hesap_ek_hesap=musteri[hesap_no_giris]['ekhesap']
                    
                    print(f'Hesap bakiyeniz : {hesap_bakiye}')  #hesap bakiyesi ve ek hesap bakiyesi basılır
                   
                    print(f'EK hesap bakiyeniz : {hesap_ek_hesap}')
                    
                    tutar = int(input('Çekmek istediğiniz tutarı giriniz : '))  #çekmek istediği tutarın girdisi alınır
                
                    hesap_para_cekme(hesap_no_giris,tutar)  #hesap_para_cekme fonksiyonuna parametreler yollanır ve işlem sonucu oradan döner
                   
                    print('*'*50)
               
                if giris_islem == '2' :     #para yatırma işlemi
                    
                    tutar = int(input('Yatırmak iistediğiniz tutarı giriniz : '))   #yatırılmak istenen tutarın girdisi alınır 
                   
                    hesap_bakiye_yatırma(hesap_no_giris,tutar)      #hesap_bakiye_yatirma fonksiyonuna parametreler gönderilir ve işlem sonucu oradan döner
               
                if giris_islem== '3' :  #para aktarma işlemi
                    
                    havale_hesap_no=int(input('Havale yapılacak kişinin hesap nosunu giriniz : '))  #paranın gönderilecek olduğu kişinin hesap_no bilgisi
                                                                                                # girdi olarak alınır
                    tutar = int(input('Havale etmek istediğiniz tutarı giriniz '))              #yatırılmak istenen tutar girdi olarak alınır

                    if havale_hesap_no in musteri:               #girilen hesap_nonun musteri sözlüğünde olup olmadığı kontrol edilir
                      
                        bakiye_aktarma(hesap_no_giris,havale_hesap_no,tutar)    #var ise bakiye_aktarma fonksiyonuna parametreler yollanır ve işlem sonucu oradan döner
                   
                    else :
                        
                        print('Böyle bir hesap no bulunamadı!') #eğer girilen hesap_no yok ise bu mesaj basılır
                
                if giris_islem== '5' :  #müşteri çıkışı
                   
                    print(f'İYİ GÜNLER DİLERİZ SAYIN {musteri_ad.upper()}.')
                   
                    break

    if islem == '3' : #program kapanışı
       
        print(musteri)
        
        print('İYİ GÜNLER........')
        
        break 
