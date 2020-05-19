import json
import os


class User :

    def __init__(self,username,password,email):

        self.username = username

        self.password = password

        self.email = email



class userRepository :
    
    def __init__(self):
        self.users = []

        self.isLoggedIn = False

        self.currentUser = {}

        self.loadUser()

    def loadUser(self):

        if os.path.exists("users.json") : #dosya varmı diye kontrol ediiyor

            with open("users.json","r",encoding="utf-8") as file :  #users.json dosyası okunuyor

                users = json.load(file) #usersın içine json stringinden dönen değerler aktarılıyor

                print(users)    #

            for userInfo in users :  #userstan gelen bilgiler döngüye giriyor ve

                userinfo =  json.loads(userInfo)    #json string bilgide python objesine dönüştürür

                newUser = User(username = userinfo['username'],password = userinfo['password'],email = userinfo['email'])
                    #user objesine dönüşüyor ve users listesine gönderiliyor
                self.users.append(newUser)
                

    def register(self,user : User):

        self.users.append(user) #kullanıcı kayıt olma user nesnesinde kabbul ediyor sadece

        self.savetoFile()

        print("Kullanıcı Oluşturuldu.")

    def login(self,username,password):
        
        for user in self.users :    #self.users listesindekiler döngüye girer

            if user.username == username and user.password == password : #ve username password inputlarında ki verilerle karşılaştırılır
                                            #eşleşme olursa giriş yapar
                self.isLoggedIn = True

                self.currentUser = user

                print("Login yapıldı.")

                break

    def logout(self):

        self.isLoggedIn = False #logout işlemi yapılırsa isloggedin false olur ve profile erişim sağlanamaz currentuser daki bilgilerde silinir

        self.currentUser = {}

        print("Çıkış Yapıldı.")

    def savetoFile(self):

        userList = []

        for i in self.users:    # self.users ta kayıtlı olan objeler döngüye sokulur 

            userList.append(json.dumps(i.__dict__)) #json string türüne dönüştürülürler

        with open("users.json","w") as file : 

            json.dump(userList , file)  #json dosyasına kayıt edilirler
    
    def identity(self):
       
        if self.isLoggedIn : #kullanıcı login yaptıysa buradan profiline erişebilir
          
            print(f"username : {self.currentUser.username}")
        
        else: 

            print("Giriş Yapılmadı")#eğer giriş yapmadan erişmeye çalışırsa bunu engeller

repository = userRepository() 

while True : 
   
    print("Menü".center(50,"*"))
    
    secim = input("1-/Register\n2-/Login\n3-/Logout\n4-/Identity  \nSeçiminiz :")

    if secim == "5" :
       #döngüden çıkış
        break
    
    else :
       
        if secim == "1":
            #kullanıcı kayıt 
            Username = input('Username : ')
            
            password = input("Password : ")
            
            email = input("email : ")
                #kullanıcıyı kayıt edebilmemiz için obje oluşturuyoruz
            user = User(username=Username , password= password , email=email)
           
            repository.register(user)
        
        elif secim == "2":
           
            if repository.isLoggedIn :
               #login yapıldıysa bir kere tekrar logini engelle
                print("Zaten giriş yaptınız")
            
            else :
                # isloggedid false ise buraya girer ve login işlemi yapılır
                Username = input('Username : ')
                
                password = input("Password : ")

                repository.login(Username,password)
       
        elif secim == "3" :
           #logout
            repository.logout()
       
        elif secim == "4":
           #profile
            repository.identity()
            
        
        else :

            print("Hatalı Tuşlama yaptınız.")

