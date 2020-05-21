import requests
import json


class movie : 

    def __init__(self):

        self.api_url = "https://api.themoviedb.org/3"   #url

        self.api_key = "9544aea9ca1c8b1ee42a32066b8c0eca"   #api key 
    
    def topRated(self):
        
        response = requests.get(self.api_url+"/movie/top_rated?api_key="+self.api_key)  #to

        response =  response.json()
        

        return response

    def popular(self) : 

        response = requests.get(self.api_url+"/movie/popular?api_key="+self.api_key)

        return response.json()

    def searchFilm(self,name):

        response = requests.get(self.api_url + "/search/company?api_key=" + self.api_key + "&query="+name)  # kullanıcıdan alınan name bilgisi ile db de arama

        return response.json()
    
    def nowPlaying(self):
        response = requests.get(self.api_url + "/movie/now_playing?api_key="+self.api_key)

        return response.json()

movi = movie()

while True : 
    print("Menü".center(75,"*"))

    operation = input("1-/TOP Rated \n2-/Popular \n3-/Search \n4-/Now Playing \n5-/Exit \nOperation : ")


    if operation == "5":

        break

    else :

        if operation == "1" :

            print('Top Rated'.center(75,"*"))

            result = movi.topRated()

            for i in result['results']:

                print(i['title'])
            
            

        elif operation == "2" : 

            print('Popular'.center(75,"*"))

            result = movi.popular()

            for i in result['results']:

                print(i['title'])

        elif operation == "3" :

            searchfilm = input('Aradığınız Filmin adını girin : ')

            result = movi.searchFilm(searchfilm)

            if len(result['results']) > 0 :

                for i in result['results']:

                    print(i['name'])

            else :

                print("\nAradığınız isim de film bulunamadı.\n")

        elif operation == "4" :
            print('Vizyondakiler'.center(75,"*"))
            result = movi.nowPlaying()

            for i in result['results'] :
                print(f"Filmin adı : {i['original_title']} \nVizyona Girdiği Tarih : {i['release_date']}")
                print("*"*20)
               
            
        else :
            print('Hatalı bir tuşlama yaptınız')