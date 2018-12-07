# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 23:46:48 2018

@author: HV
"""
# part 2
file = open("day7.txt")
seq = list()
chars = set()
for line in file:
    pre = line.split(" ")[1]
    nxt = line.split(" ")[7]
    seq.append([pre,nxt])
    chars.add(pre)
    chars.add(nxt)
    
def getUnconstraintChars(pairs, chars):
    candidateCharList = list()
    for char in chars:
        find = False
        for pair in pairs:
            if char == pair[1]:
                find = True
                break
        if not find:
            candidateCharList.append(char)
            
    return sorted(candidateCharList)

result = str("")
time = 0
# 建立任务列表
tasks = dict()
points = set()
for point in seq:
    if point[0] not in points:
        points.add(point[0])
    if point[1] not in points:
        points.add(point[1])

for point in points:
    # Example
    #tasks[point] = ord(point) - ord('A') + 1 
    # Real
    tasks[point] = 60 + ord(point) - ord('A') + 1 


avaliableWorkers = 5
works = list() # 正在执行的工作
while(len(seq) > 0):
    # 有待选的任务
    candidateTasks= getUnconstraintChars(seq, chars)
    
    # 待选任务分配给可用的工人
    if  avaliableWorkers >=len(candidateTasks):
        #从待选的任务中拿出前 avaliableWorkers 个 来完成
        works += candidateTasks[:avaliableWorkers]
        avaliableWorkers -= len(candidateTasks)
    else:
        # 工人数 没有工作 多
        # 那就拿出 工作人数那么多个工作出来
        works += candidateTasks[:avaliableWorkers]
        avaliableWorkers = 0
        
    # 对工作的时间进行排序，最快的先完成，从tasks中剔除出去，（注意同时完成的工作）
    minWorkTime = 100
    minWork = list()
    # 找到最快能够完成的时间
    for work in works:
        workTime = tasks[work]
        if workTime < minWorkTime:
            minWorkTime = workTime
    # 找到最快能够完成的工作/任务        
    for work in works:
        workTime = tasks[work]
        if workTime == minWorkTime:
            minWork.append(work)

    # 大家都疯狂干工作，工作时间是 minWorkTime
    for task in works:
        if tasks[task] > 0:
            tasks[task] -= minWorkTime
    
    # 从work里清楚已经完成的工作
    for i in minWork:
        if i in works:
            works.remove(i)
    
    # 总的运行时间
    time += minWorkTime
    
    # 工作做完了，空出来我们的工人
    avaliableWorkers += len(minWork)
    
   # 从chars 和 seq 中 清除 minWork 对应的工作
    temSeq = list()
    for item in seq:
        if item[0] in  minWork:
            if item[0] in chars:
                chars.remove(item[0])
        else:
            temSeq.append(item)
            
    seq = temSeq
    
# 最后一个工作的时间
for task in tasks:
    if tasks[task] != 0:
        time += tasks[task]
print(time)