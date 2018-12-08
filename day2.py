# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:19:07 2018

@author: RV
"""

"""
计算字符串中是某有出现了2次或者3次的字符
思路：
1. 计算每个字符出现的次数
用map 来实现？
"""
def checkif(boxId):
    m = 0
    n = 0
    dic = dict()
    for index in range(0,len(boxId)):
        if boxId[index] in dic:
            dic[boxId[index]] += 1
        else:
            dic[boxId[index]] = 1
            
    # 找到出现两次、三次的字符
    for x in dic:
        if(dic[x] == 2):
            m = 1
        elif(dic[x]==3):
            n = 1
    return [m,n]


file = open("day2.txt","r")

# ID中字母出现两次的盒子数
twoOC = 0;
# ID中字母出现3次的盒子数
threeOC = 0;

for line in file:
    [x,y] = checkif(line)
    twoOC += x
    threeOC += y

file.close()    
    
# 计算checksum
checksum = twoOC * threeOC

print(checksum)





    