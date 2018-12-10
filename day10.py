# -*- coding: utf-8 -*-
"""
Created on Sun Dec  10 15:28:30 2018

@author: RV
"""
import re
file = open('day10.txt','r')
positions = []
velocities = []
for line in file:
    [x,y,vx,vy] = list(map(int, re.findall(r"[-\d]+",line)))
    positions.append([x,y])
    velocities.append([vx,vy])

def getImage(positions):
    x0 = min(x[0] for x in positions)
    x1 = max(x[0] for x in positions)
    y0 = min(x[1] for x in positions)
    y1 = max(x[1] for x in positions)
    dx = x1 - x0
    dy = y1 - y0
    #return (dx,dy)
    # return (x0,x1,y0,y1)
    # print(x0,x1,y0,y1)
    rows = []
    for x in range(x0,x1+1):
        row = []
        for y in range(y0,y1+1):
            if [x,y] in positions:
                row.append('#')
            else:
                row.append('.')
        rows.append(''.join(row))
    return '\n'.join(rows)
second = 0
while True:
    second += 1
	# find the minimal distance between points
	# that would be the second when we can see the message
    if abs(second - 10477) < 3:
        print(second)
        print(getImage(positions))
        # print("LLLL")

    # update points positions
    for i in range(len(positions)):
        positions[i] = [positions[i][0]+ velocities[i][0],positions[i][1] + velocities[i][1]]
