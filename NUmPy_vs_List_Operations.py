# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:22:21 2022

@author: bobbala
"""

import numpy as np
import time 
import sys


SIZE = 1000

lis = range(SIZE)

print("Size taken by list:", sys.getsizeof(lis[4]) * len(lis))

np_arr = np.arange(SIZE)
print("Size taken by np array:",np_arr.size * np_arr.itemsize)



SIZE = 1000000

list1 = range(SIZE)
list2 = range(SIZE)
list3 = []

start_time = time.time()
# for i in range(SIZE): 
#     list3.append(list1[i]+list2[i])

result = [(x+y) for x,y in zip(list1, list2)]
end_time = time.time()

print("Time Took for List operation:", (end_time - start_time)*1000)

np1 = np.arange(SIZE)
np2 = np.arange(SIZE)

start_time = time.time()
np3 = np1+np2
end_time = time.time()

print("Time Took for Numpy operation:", (end_time - start_time)*1000)