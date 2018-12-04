# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:18:34 2018

@author: HV
"""
import re
from operator import add
file = open("day4.txt","r")

record = dict()
for line in file:
    (time,content) = [t(s) for t,s in zip((str,str), re.search('^(\[.+\] )(.+)$',str(line)).groups())]
    if(time in record):
        print("It's not right list")
    else:
        record[time] = content
file.close()

# 第一步：获取排序之后的记录
sortedRecord = list()
outFile = open("test.txt","w")
for key in sorted(record):
    sortedRecord.append((key,record[key]))
    outFile.write(key + record[key] + '\n')
    
outFile.close()
guards = dict()
guardID = str(" ")

for rec in sortedRecord:
    time = rec[0]
    state = rec[1]
    if(state[0] is 'G'):
        guardID = re.search('^Guard.#([\d.]+) begins shift',str(state)).groups()
        if(guardID not in guards):
            onehourList = [0]*60
            guards[guardID]  = onehourList
    elif(state[0] is 'f'):
        timeBeginSleep = int(re.search('^\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\].$',str(time)).groups()[0])
        for i in range(timeBeginSleep,60):
            guards[guardID][i]  += 1
    elif(state[0] is 'w'):
        timeBeginAwake= int(re.search('^\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\].$',str(time)).groups()[0])
        for i in range(timeBeginAwake,60):
            guards[guardID][i]  -= 1

# part 1
mostlazyGruadID = -1        
mostSleepTime = 0
mostSuitHour = -1
for guard in guards:
    sleeptime = sum(guards[guard])
    if mostSleepTime < sleeptime:
        mostSleepTime  = sleeptime
        # 获取最懒guard的ID
        mostlazyGruadID = int(guard[0])
        # 获取那个重合最多
        mostSuitHour = guards[guard].index(max(guards[guard]))
        
print(int(mostlazyGruadID) * int(mostSuitHour))




# part 2
"""
找到频率最高的那个ID和次数
"""
mostmost = 0
output = 0
for guard in guards:
    index = guards[guard].index(max(guards[guard]))
    lazyguard = int(guard[0])
    result = index * lazyguard
    if mostmost < guards[guard][index]:
        output = result
        mostmost = guards[guard][index]
        
        
print(output)


"""
文中只给出了两种方案，下面是我自己想的一种方案的解法。
我想的方案是这样的：
找到所有guard在哪个时刻最容易睡着(也就是在哪个时刻睡着的次数最多，通过的概率肯定也就最大啊)
然后找到那一时刻，睡着次数最多的guard
算出guard's ID * times of asleep of that moment
"""
# part 2
countList = [0]*60
for guard in guards:
    countList = list(map(add,countList, guards[guard]))
    
inx = countList.index(max(countList))

mostTimes = 0
mostlazyGruadID = -1
for guard in guards:
    times = guards[guard][inx]
    if mostTimes < times:
        mostTimes = times
        mostlazyGruadID = int(guard[0])
        
print(mostlazyGruadID * mostTimes)