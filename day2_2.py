# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:17:30 2018

@author: RV
"""

file = open("day2.txt","r")

def check(id1, id2):
    if(len(id1) != len(id2)):
        return 0,0
    count = len(id1)
    length = count
    unsameIndex = -1
    
    for index in range(0,length):
        if(id1[index] is id2[index]):
            count -= 1
        else:
            unsameIndex = index
    
    return count == 1,unsameIndex



boxIDs = [];
for boxID in file.readlines():
    boxIDs.append(boxID)
    
for i in range(0,len(boxIDs)-1):
    for j in range(i+1,len(boxIDs)):
        x,y = check(boxIDs[i],boxIDs[j])
        if(x):
            print(boxIDs[i])
            print(boxIDs[j])
            print(y)
            
file.close()