# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:20:08 2018

@author: RV
"""

lines = open("day18.txt").read().split('\n')
ground   = list()

for i in range(len(lines)):
    row = list()
    for j in range(len(lines[0])):
       row.append(lines[i][j])
    ground.append(row)
minute = 0
# part 1 
# maxIter = 10
# part 2
maxIter = 1000

result = 0
while minute < maxIter:
    # python 里面 = 还有 reference的作用么？
    tmpGround = []
    for row in range(len(ground)):
        new = []
        for column in range(len(ground[0])):
            new.append(ground[row][column])
        tmpGround.append(new)
       
    for row in range(len(ground)):
        for column in range(len(ground[0])):
            d = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
            nb  = [[row+x,column+y] for x,y in d if row+x >= 0 and row+x < len(ground) and column+y >=0 and column +y <len(ground[0])]
            
            # 计算周围树和伐木场的个数
            numTrees = 0
            numLumberyard  = 0
            for x,y in nb:
                if ground[x][y] == '|':
                    numTrees += 1
                elif ground[x][y] == '#':
                    numLumberyard += 1
            # 更新tmpGround
            if ground[row][column] == '.': 
                if numTrees >= 3:
                    tmpGround[row][column] = '|'
            elif ground[row][column] == '|':
                if numLumberyard >= 3:
                    tmpGround[row][column] = '#'
            elif ground[row][column] == '#':
                if numTrees >= 1 and numLumberyard >= 1:
                    tmpGround[row][column] = '#'
                else:
                    tmpGround[row][column] = '.'
                    
    
    ground = [y for y in [x for x in tmpGround]]
    minute += 1

    # print("After %d minutes:", minute)
    woudedArces = 0
    numLumberyards  = 0
    for row in range(len(ground)):
        for col in range(len(ground[0])):
            if ground[row][col] == '|':
                woudedArces +=1
            elif ground[row][col] == '#':
                numLumberyards += 1

    currResult = numLumberyards * woudedArces        
    delta = currResult - result
    if (delta == 413):
        # 保留上一时刻 minute 和 result
        x = minute-1
        break
    result = currResult
    # print("Result: ",currResult,"Delta:",delta)
    # print(delta,end = ' ')
    # for g in ground:
    #     print(''.join(g))

change = "413 3655 1194 1494 -4772 -1371 -5953 -3550 -7754 -3294 -4226 2378 -1566 5400 3152 6463 3477 7536 4809 1860 493 1647 -375 13 -1190 -12535 -1351 3953"
cycle = list(map(int,change.split(' ')))
length = len(cycle)
suma = sum(cycle)
minutesNum = 1000000000 
cycleLen = minutesNum - x
resourceValue = result
resourceValue += int(cycleLen/length) * suma + sum(cycle[:cycleLen%length])
print(resourceValue)