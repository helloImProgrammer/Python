# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:45:57 2020

@author: cihan
"""

import numpy as np 

#python list

list1 = [1,2,3,4,5,6,7,8,9]

np_array = np.array([1,2,3,4,5,6,7,8,9])  #array tanımlaması


print(type(list1))
print(type(np_array))


py_multi_list = [[1,2,3],[4,5,6],[7,8,9]]

np_multi_array = np_array.reshape(3,3) #diziyi 3e 3lük matris haline çevirdi

print(py_multi_list)
print(np_multi_array)


print(np_array.ndim)

print(np_multi_array.ndim)  #dizinin boyutunu bize verir


print(np_array.shape)           # dizinin kaça kaçlık boyutu olduğunu bize verir
print(np_multi_array.shape)