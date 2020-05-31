# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:08:10 2020

@author: cihan
"""

import numpy as np 


#result = np.array([1,2,3,4,5,6,7,8,9])

#result = np.arange(12)

#result  = np.arange(5,100,5) #arange() başlangıç ve bitiş değeri arasındaki değerleri belirtilen değer de arttırarak
#bize liste olarak dönmesini sağladık

#result  = np.zeros(10) # 10 tane sıfır döndürür bize

#result = np.ones(10) #10 tane 1 verir

result = np.linspace(0,100,5) # verdiğimiz başlangıç ve bitiş değeri arasında belirttiğimiz şekilde bölerek
# bize döndürür

result = np.random.randint(20) # rastgele sayı üretir

result = np.random.randint(1,10,3) #bize başlangıç ve bitiş değeri arasında belirttiğimiz adette 
# rastgele sayı üreterek bize döndürür

result = np.random.rand(5) #float değerler üretir

result = np.random.randn(5) # negatif float değerler üretir


np_array = np.arange(55)  
np_multi = np_array.reshape(5,11) #5*11 lik bibr matris üretir
print(np_multi.sum(axis=1))     # matrisin satırlarının toplamını döndürür
print(np_multi.sum(axis=0)) #matrisin sütunlarını döndürür
 
rnd_numbers = np.random.randint(1,200,15)
print(rnd_numbers)
result = rnd_numbers.max()  #dizide ki en yüksek sayıyı verir
result = rnd_numbers.min()  #dizide ki en küçük sayıyı verir
result = rnd_numbers.mean() #dizinin ortalamasını verir
result = rnd_numbers.argmax()   #dizide ki en yüksek sayının indeksini verir
result = rnd_numbers.argmin()   #dizide ki en küçük sayının indeksini verir
    
print(result)