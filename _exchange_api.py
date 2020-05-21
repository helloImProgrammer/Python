import requests
import json



url = ("https://api.exchangeratesapi.io/latest")
result = requests.get(url)

result =json.loads(result.text)
print("Para birimleri : \n")
print(result["rates"].keys())

unit = input("Bozulan döviz türü : ").upper()
currency = input("Alınan döviz türü : ").upper()
amount = float(input("Ne kadar dönüştürmek istiyorsunuz : "))




print("1 {0} : {1} {2}".format(unit,result["rates"][currency],currency))

print("{0} {1} = {2} {3}".format(amount , unit , amount * result["rates"][currency] ,currency))