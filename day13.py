# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:18:31 2018

@author: RV
"""
class Car(object):
    def __init__(self,position,direction):
        self.position = position
        self.direction = direction
        self.crossMode = 0
        self.alive = True
    
    def __lt__(self, other):
        return self.position[1]  < other.position[1]
    
    def getCar(self):
        return self.position, self.direction, self.crossMode, self.alive
    
    def getPosition(self):
        return self.position

    def setCar(self,position,direction,mode, isAlive):
        self.position = position
        self.direction = direction
        self.crossMode = mode
        self.alive = isAlive
    def setIsAlive(self, isAlive):
        self.alive = isAlive
        
    def isAlive(self):
        return self.alive
    
# update position 这是一个tick
def updatePosition(cars, trackMap):
        roadCornor = ['\\','/','+']
        for car in cars:
            position,direction, crossMode, isAlive = car.getCar()
            
            # 更新位置
            position = [position[0] + direction[0], position[1]+direction[1]]
            # 更新方向
            rodState = trackMap[position[1]][position[0]]
            if rodState in roadCornor:
                if rodState == '\\':
                    direction[0], direction[1] = direction[1], direction[0]
                elif rodState == '/':
                    direction[0], direction[1] = -direction[1], -direction[0]
                elif rodState == '+':
                    if crossMode == 0 :
                        direction[0], direction[1] = direction[1], -direction[0]
                    elif crossMode == 2:
                        direction[0], direction[1] = -direction[1], direction[0]
                    crossMode = (crossMode+1) % 3
            # 设置状态   
            car.setCar(position,direction,crossMode,isAlive)
            
# collsiion detection
def collisionDetection(cars, trackMap):
    for index in range(len(cars)-1):
        position1= cars[index].getPosition()
        #print(position1)
        for cp in range(index+1, len(cars)):
            position2 = cars[cp].getPosition()
           # print(position2)
            if position1 == position2:
                #print ("Collision pos: ", position1)
                cars[index].setIsAlive(False)
                cars[cp].setIsAlive(False)
                
        siezAliveCars = len(cars)
        for car in cars:
            if not car.isAlive():
                siezAliveCars -= 1
                
        return siezAliveCars == 1
            
def main():
    file = open("day13.txt","r")
    
    direction = ['>','<','v','^']
    trackMap = list()
    cars = list()
    
    row = 0
    column = 0
    for line in file:
        trackMap.append(line.strip('\n'))
        column = 0
        for d in line:
            if d in direction:
                d = {'>':[1,0],'<':[-1,0],'v':[0,1],'^':[0,-1]}[d]
                cars.append(Car([column,row],d))                      
            column += 1 # j column
        row +=1 # i row    
    cars.sort()
    
    collision = False
    tick = 0
    while not collision:
        collision = collisionDetection(cars, trackMap)
        
        if collision :
            for car in cars:
                if car.isAlive():
                    print(car.getPosition())
                    
            break
        else:
            updatePosition(cars, trackMap)
            tick += 1


if __name__ == '__main__':
    main()