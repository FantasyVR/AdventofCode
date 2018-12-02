# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:53:40 2018

@author: HV
"""

file = open("day1.txt","r")

freset = set()
frequency = 0;

frelist = []
for line in file:
    frelist.append(int(line))
    
    
find = 0
while(1):
    for fre in frelist:
        frequency += fre
        if frequency not in freset:
            freset.add(frequency)
        else:
            print(frequency)
            find = 1
            break
    
    if(find == 1):
        break

    
file.close()    