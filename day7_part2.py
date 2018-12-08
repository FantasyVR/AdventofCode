# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 23:46:48 2018

@author: RV
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

# 总时间
totalTime = 0
points = set()
for point in seq:
    if point[0] not in points:
        points.add(point[0])
    if point[1] not in points:
        points.add(point[1])

# 建立任务列表
tasks = dict()
for point in points:
    # Example
    #tasks[point] = ord(point) - ord('A') + 1 
    # Real
    tasks[point] = 60 + ord(point) - ord('A') + 1 

avaliableWorkers = 5
currentWorks = list() # 正在执行的工作
while(len(seq) > 0):
    # 有待选的任务, 这个求待选任务的函数输入参数应该不包含目前的 已经在做的工作
    candidateTasks= getUnconstraintChars(seq, chars)
    
    # 待选任务分配给可用的工人
    if  avaliableWorkers >=len(candidateTasks):
        #从待选的任务中拿出前 avaliableWorkers 个 来完成
        currentWorks += candidateTasks[:avaliableWorkers]
        avaliableWorkers -= len(candidateTasks)
    else:
        # 工人数 < 任务数
        # 那就拿出 工作人数那么多个工作出来
        currentWorks += candidateTasks[:avaliableWorkers]
        avaliableWorkers = 0
        
        
    # 从chars 和 seq 中 清除 currentWork 对应的工作
    for work in currentWorks:
       if work in chars:
           chars.remove(work)
           
    temSeq = list()
    for item in seq:
        if item[0] not in  currentWorks:
            temSeq.append(item)    
    seq = temSeq
    
    # 对工作的时间进行排序，最快的先完成，从tasks中剔除出去，（注意同时完成的工作）
    minWorkTime = 1000
    minWork = list()
    # 找到所有目前工作中 最快能够完成的时间
    for work in currentWorks:
        workTime = tasks[work]
        if workTime < minWorkTime:
            minWorkTime = workTime
    # 找到最快能够完成的工作/任务        
    for work in currentWorks:
        workTime = tasks[work]
        if workTime == minWorkTime:
            minWork.append(work)

    # 大家都疯狂干工作，工作时间是 minWorkTime
    for work in currentWorks:
        if tasks[work] > 0:
            tasks[work] -= minWorkTime
    
    # 从work里清楚已经完成的工作
    for i in minWork:
        if i in currentWorks:
            currentWorks.remove(i)
    
    # 总的运行时间
    totalTime += minWorkTime
    
    # 工作做完了，空出来我们的工人
    avaliableWorkers += len(minWork)
    

    
# 最后一个工作的时间
for task in tasks:
    if tasks[task] != 0:
        totalTime += tasks[task]
print(totalTime)