# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 15:07:27 2018

@author: RV
"""

file = open("day1.txt","r")


frequency = 0;
for line in file:
    frequency += int(line)
    
file.close()    
print(frequency)