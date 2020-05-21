import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")


result = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit = 10)
print("Top Rated Movie".center(75,"*"))
for tr in result : 
    title = tr.find("td",{"class":"titleColumn"}).find("a").string
    year = tr.find("td",{"class":"titleColumn"}).find("span").string.strip("()")
    score = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").string
    print(f"Name : {title} \nYear : {year} \nIMDB score : {score}")
    print("*"*50)