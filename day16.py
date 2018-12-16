# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 20:12:59 2018

@author: RV
"""
from collections import defaultdict
opType = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

opCodeMap = defaultdict(set)

def compute(opCode, bf,opT):
    before = [x for x in bf ]
    # register A,B,C,D
    [rA, rB, rC, rD] = before
    # op sourceData1 sourceData2, destination
    [op, s1, s2, d] = opCode
    if opT == 'addr':
        before[d] = before[s1] + before[s2]
    elif opT == 'addi':
        before[d] = before[s1] + s2
    elif opT == 'mulr':
        before[d] = before[s1] * before[s2]
    elif opT == 'muli':
        before[d] = before[s1] * s2
    elif opT == 'banr':
        before[d] = before[s1] & before[s2]
    elif opT == 'bani':
        before[d] = before[s1] & s2
    elif opT == 'borr':
        before[d] = before[s1] | before[s2]
    elif opT == 'bori':
        before[d] = before[s1] | s2
    elif opT == 'setr':
        before[d] = before[s1]
    elif opT == 'seti':
        before[d] = s1
    elif opT == 'gtir':
        if s1 > before[s2]:
            before[d]  = 1
        else:
            before[d]  = 0
    elif opT == 'gtri':
        if before[s1] > s2:
            before[d] =  1
        else:
            before[d] = 0
    elif opT == 'gtrr':
        if before[s1] > before[s2]:
            before[d] = 1
        else:
            before[d] = 0
    elif opT == 'eqir':
        if s1 == before[s2]:
            before[d] = 1
        else:
            before[d] = 0
    elif opT == 'eqri':
        if before[s1] == s2:
            before[d] = 1
        else:
            before[d] = 0
    elif opT == 'eqrr':
        if before[s1] == before[s2]:
            before[d]  = 1
        else:
            before[d]  = 0   
    return before

def isSuit(opCode, bf, after, opT):
    return after == compute(opCode, bf,opT)


def test(opCode, bf, after):
    count = 0
    for opT in opType:
        if isSuit(opCode,bf,after,opT):
            count+=1
            opCodeMap[opT].add(opCode[0])
        
    return count >= 3

import re
file = open("day16_1.txt")

beforeList = list()
afterList = list()
opList = list()
for line in file:
    if "Before" in line:
        bf = list(map(int,re.findall("[\d]+",line)))
        beforeList.append(bf)
    elif "After" in line:
        after = list(map(int,re.findall("[\d]+",line)))
        afterList.append(after)
    elif line not in ['\n', '\r\n']:
        opCode = list(map(int,line.strip().split(' ')))
        opList.append(opCode)
        
length = len(beforeList)       
# 一条指令3种以上解释
num = 0

for index in range(length):
    bf, after, op = beforeList[index], afterList[index], opList[index]
    if test(op, bf, after):
        num += 1
        
print(num)


rightMap = defaultdict(int)
# part 2
#for i in opCodeMap:
#    print(i, ": ", opCodeMap[i])
while True:  
    for i in opCodeMap:
        if len(opCodeMap[i]) == 0:
            continue
        elif len(opCodeMap[i]) == 1:
            rightMap[i] = opCodeMap[i].pop()
        else:
            for rm in rightMap:
                if rightMap[rm] in opCodeMap[i]:
                    opCodeMap[i].remove(rightMap[rm])
    count = 0            
    for i in opCodeMap:
        if len(opCodeMap[i]) > 0:
            count += 1
                
    if count == 0:
        break
            
revertMap = defaultdict(str)
for i in rightMap:
    #print(i, ": ", rightMap[i])
    revertMap[rightMap[i]] = i
    
instruction =  open("day16.txt").read().split("\n")

bf = afterList[-1]
bf = [0,0,0,0]
for ins in instruction:
    opCode = list(map(int,ins.split(' ')))
    bf = compute(opCode,bf,revertMap[opCode[0]])

print(bf)