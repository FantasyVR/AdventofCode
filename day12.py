# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:13:56 2018

@author: RV
"""
from collections import defaultdict

def getSum(state,left):
    result = 0
    for i in range(len(state)):
        #print(state[i])
        if state[i] == '#':
            result += i - left
        

    return result


file = open("day12.txt","r")

initState = file.readline().split(" ")[2][:-1]

line0 = file.readline()

rule = defaultdict(str)
for line in file:
    pre,net = line.split(" ")[0], line.split(" ")[2][0]
    rule[pre] = net
    #print(pre," ==> ",net)

    
generation = 0
maxGen = 110
left = 5
right = 300
state ='.'*left +  initState + '.'*right
lastresult = 0
#print(state)
while(generation < maxGen):
    #print("Generation:", generation,":",state)
    tmp = state[:2]
    for i in range(2,len(state)-2):
        du = state[i-2:i+3] # range:5
        if du in rule:
            result = rule[du]
            tmp += result
            #print(i,"  ",du," => ",result)
        else:
            tmp += '.'
    tmp += state[-2:]
    
    state = ''.join(str(v) for v in tmp)
    generation +=1
    
    result = getSum(state,left)
    dr = result - lastresult
    lastresult = result
    #print(dr,end= ' ')
    print(result, end = ' ')
    
    

part2Gen = 50000000000
scores = (part2Gen-maxGen) * 59 + result
print(scores)

