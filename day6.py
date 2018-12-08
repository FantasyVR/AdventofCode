# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:09:13 2018

@author: RV
"""
import sys
def computeDistance(coor, point):
    return abs(point[0] - coor[0]) + abs(point[1] - coor[1])

def computeTotoalDis(coor, points):
    distance = 0
    for point in points:
        distance += computeDistance(coor,point)
    return distance



file = open("day6.txt")

# 读入的各个采样点
points = list()
for line in file.readlines():
    [x,y] = map(int, line.split(','))
    points.append([x,y])
    
[xlist, ylist]  = zip(*points)
[minx,miny,maxx,maxy] = [min(xlist),min(ylist),max(xlist),max(ylist)]
print(minx, miny,maxx,maxy)




# part 1
# grid  key: coordinates value: [pointIndex,mindistance]
grid = dict()
for i in range(minx,maxx+1):
    for j in range(miny,maxy+1):
        grid[(i,j)] = [-1,sys.maxsize];
# 找到网格上每个坐标 离得最近的那个点的索引值和距离值， 如果同时离两个或者以上的点距离相同，则不属于任何一个点，pointIndex设置成-2
for gridCoord in grid:
    # 当网格上坐标离两个point最小距离相同，则跳过
    if(grid[gridCoord][0] == -2):
        continue
    
    mincoordindex = grid[gridCoord][0]
    mindistance   = grid[gridCoord][1]

    for index in range(len(points)):
        position = points[index]
        distance = computeDistance(gridCoord,position)
        if distance < mindistance:
            mindistance = distance
            mincoordindex = index
        elif distance == mindistance:
            mincoordindex = -2
    
    grid[gridCoord]  = [mincoordindex,mindistance]
    
# boundaryPointset:边界上的点的 pointIndex
boundaryPointset = set()
for i in range(minx,maxx):
    boundarypoint = grid[(i,miny)][0]
    boundaryPointset.add(boundarypoint)
for i in range(minx,maxx):
    boundarypoint = grid[(i,maxy)][0]
    boundaryPointset.add(boundarypoint)
for j in range(miny,maxy):
    boundarypoint = grid[(minx,j)][0]
    boundaryPointset.add(boundarypoint)
for j in range(miny,maxy):
    boundarypoint = grid[(maxx,j)][0]
    boundaryPointset.add(boundarypoint)    

candidateCoord = list()    
for i in range(len(points)):
    if i not in boundaryPointset:
        candidateCoord.append(points[i])
        
# 算出内部每个点的最大面积
# aredic key : pointIndex value: area
areadic = dict()
for coord in grid:
    # 如果在边界上，则面积无穷大，跳过计算
    if grid[coord][0] in boundaryPointset:
        continue
    if grid[coord][0] in areadic:
        areadic[grid[coord][0]] += 1
    else:
        areadic[grid[coord][0]] = 1

# sortedArea key:area value: pointIndex
sortedArea = sorted(areadic.items(),key = lambda x : x[1])
for i in sortedArea:
    print(i)
"""
[x,y] = [0,0]
for point in points:
    x += point[0]
    y += point[1]

origin = [int(x/len(points)),int(y/len(points))]
region = 0
for x in range(origin[0],maxx):
    distance = computeTotoalDis([x, origin[1]],points)
    if distance < 10000:
        region += 1
    else:
        break
    for y in range(origin[1]+1,maxy):
        distance = computeTotoalDis([x,y],points)
        if(distance < 10000):
            region +=1
        else:
            break
    
for x in range(origin[0],maxx):
    distance = computeTotoalDis([x, origin[1]-1],points)
    if distance < 10000:
        region += 1
    else:
        break
    for y in reversed(range(miny,origin[1]-1)):
        distance = computeTotoalDis([x,y],points)
        if(distance < 10000):
            region +=1
        else:
            break

for x in reversed(range(minx,origin[0]-1)):
    distance = computeTotoalDis([x, origin[1]],points)
    if distance < 10000:
        region += 1
    else:
        break
    for y in range(origin[1]+1,maxy):
        distance = computeTotoalDis([x,y],points)
        if(distance < 10000):
            region +=1
        else:
            break

for x in reversed(range(minx,origin[0]-1)):
    distance = computeTotoalDis([x, origin[1]],points)
    if distance < 10000:
        region += 1
    else:
        break
    for y in reversed(range(miny,origin[1]-1)):
        distance = computeTotoalDis([x,y],points)
        if(distance < 10000):
            region +=1
        else:
            break

print(region)
"""

# part 2
region = 0
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        distance = computeTotoalDis([x,y],points)
        if(distance < 10000):
            region += 1
         
print (region)