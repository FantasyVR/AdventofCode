# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:15:15 2018

@author: RV
"""
# part 1
def computePowerLevel( cell , serialNum):
    x = cell[0]
    y = cell[1]
    rackID = x + 10
    powerLevel = rackID * y + serialNum
    powerLevel *= rackID
    if powerLevel < 100:
        return 0
    digit = int(powerLevel / 100) % 10
    return digit - 5



grid = dict()
sn = 7165
for i  in range(1,301):
    for j in range(1,301):
        grid[(i,j)] = computePowerLevel([i,j],sn)
        
largetstTP = 0
largetsCell= [0,0]
for i in range(1,301-3):
    for j in range(1,301-3):
        tp = 0
        for index in range(i,i+3):
            for xx in range(j,j+3):
                tp += grid[(index,xx)]
        if tp > largetstTP:
            largetstTP = tp
            largetsCell = [i,j]
            
print(largetsCell)


# part 2
agrid = [[0]*300 for i in range(300)]
for i in range(0,300):
	for j in range(0,300):
		agrid[i][j]  = grid[(i+1,j+1)]
 
def generateAux(originM):
    auxM = [[0]*300 for i in range(300)]
    # auxM first column equal originM's colum
    for i in range(300):
        auxM[0][i]  = originM[0][i]
    # column wise 
    for i in range(1,300):
        for j in range(300):
            auxM[i][j]  = originM[i][j] + auxM[i-1][j]
    # row wise
    for i in range(300):
        for j in range(1,300):
            auxM[i][j] += auxM[i][j-1]
    return auxM

def sumQuary(auxM, coordinate, length):
    tli,tlj,rbi,rbj = coordinate[0],coordinate[1],coordinate[0]+length,coordinate[1]+length
    res = auxM[rbi][rbj]
    if tli > 0:
        res -= auxM[tli-1][rbj]
    if tlj > 0:
        res -= auxM[rbi][tlj-1]
    if tli > 0 and tlj>0:
        res += auxM[tli-1][tlj-1]

    return res

print("Starting generate Aux Matrix")
auxM = generateAux(agrid)
print("Aux Matrix is generated")

sideLen = 0
maxSum = 0
maxCell = [0,0,sideLen]

while(sideLen < 300):
    for i in range(0,300-sideLen):
        for j in range(0,300-sideLen):
            res = sumQuary(auxM,[i,j], sideLen)
            if res > maxSum:
                maxSum  = res
                maxCell = [i+1,j+1,sideLen+1]
    sideLen += 1
print("largest total square: ",maxSum)
print("identifier",maxCell)





# part 2 
# step = 0
# largetstTP = 0
# largetsCell= [0,0,step]
# while(step < 300):
#     for i in range(1,301-step):
#         for j in range(1,301-step):
#             tp = 0
#             for index in range(i,i+step):
#                 for xx in range(j,j+step):
#                     tp += agrid[index][xx]
#             if tp > largetstTP:
#                 largetstTP = tp
#                 largetsCell = [i,j,step]
    
#     step += 1
#     print("Starting step size: " , step)
          
# print(largetsCell)                


# improved method 1
# step = 0
# largetstTP = 0
# largetsCell= [0,0,step] 
# cell = dict()
# while(step < 300):
#     for i in range(1,301-step):
#         for j in range(1,301-step):
#             tp = cell[(i,j)][0]
#             preStep = cell[(i,j)][1]
#             for index in range(i+preStep,i+step):
#                 for xx in range(j+preStep,j+step):
#                     tp += agrid[index-1][xx-1]
#             cell[(i,j)] = [tp, step]
#             if tp > largetstTP:
#                 largetstTP = tp
#                 largetsCell = [i,j,step]
    
#     step += 1
#     print("Starting step size: " , step)
          
# print(largetsCell)    