# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:28:30 2018

@author: RV
"""
"""
At first, I used list. But it's to slow to solve part 2
So, I found blist.
It's more efficient for inserting O(logn).
"""
import blist

numPlayer = 476 
lastMarble  = 7143100 

gameList = blist()
scores = [0] * numPlayer

marbalIndex = 0
gameList.append(marbalIndex)

current = 0
while(marbalIndex <= lastMarble):
    for i in range(numPlayer):
        
        marbalIndex += 1
        
        if marbalIndex > lastMarble:
            break
        
        if marbalIndex % 23 == 0:
            scores[i]  += marbalIndex
            # the marble 7 marbles counter-clockwise from the current marble is removed from the circle
            if current - 7 >=0:
                scores[i] += gameList[current - 7]
                gameList = gameList[: current-7] + gameList[current-6:]
                current = current - 7
            else:
                scores[i] += gameList[current-7]
                tmp  = len(gameList) + current - 7
                gameList = gameList[:current-7] + gameList[len(gameList) + current - 7+1:]  
                current = tmp
            continue
        
        if len(gameList) == current + 1:
            gameList.insert(1,marbalIndex)
            current = 1
        else:
            gameList.insert(current+2,marbalIndex)
            current += 2 
    
highScore = 0
for score in scores:
    if score > highScore:
        highScore = score       
print(highScore)