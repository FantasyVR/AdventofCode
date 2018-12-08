# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:07:10 2018

@author: RV
"""
def getUnconstraintChar(pairs, chars):
    candidateCharList = list()
    for char in chars:
        find = False
        for pair in pairs:
            if char == pair[1]:
                find = True
                break
        if not find:
            candidateCharList.append(char)
    return sorted(candidateCharList)[0]

"""
思路：
1. 提取出steps: [preStep, nextStep]
2. 提取出 chars:路径点的集合set表示（不可重复）
3. 如果 steps 没有走完，那么继续走第四步，否则直接退出，输出结果
4. 将没有约束的steps排序，按字母表排序，走第一个，也就是函数的返回值
5. 将这个字母从路径点chars中删除，将以该字母为前提的step删除
注意问题：
最后一步问题
"""
file = open("day7.txt","r")
seq = list()
chars = set()
for line in file:
    pre = line.split(" ")[1]
    nxt = line.split(" ")[7]
    seq.append([pre,nxt])
    chars.add(pre)
    chars.add(nxt)

result = str("")
while(len(seq)>1):
    hihi = getUnconstraintChar(seq, chars)
    result += hihi
    temSeq = list()
    for item in seq:
        if item[0] == hihi:
            if hihi in chars:
                chars.remove(hihi)
        else:
            temSeq.append(item)            
    seq = temSeq
    
finalstep = seq
result += finalstep[0][0]
result += finalstep[0][1]

print(result)