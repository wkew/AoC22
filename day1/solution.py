# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:29:23 2022

@author: Will Kew
@email: will.kew[at]gmail.com
"""



import numpy as np

dataloc = r'D:\Coding\AoC22\day1/'

with open(dataloc+'input.txt') as f:
    lines = f.readlines()
    
i = 0
all_data = []
curlist = []
for element in lines:
    if element == '\n':
        i+=1 
        all_data.append(curlist)
        curlist = []
    else:
        curlist.append(int(element.split('\n')[0]))

all_sum = []
for element in all_data:
    all_sum.append(np.sum(element))
    
print(max(all_sum))

### Part 2

all_sum.sort(reverse=True)

print(np.sum(all_sum[:3]))
