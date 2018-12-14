# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:59:40 2018

@author: RV
"""

# part 1
fec = 0
sec = 1
recipes = [3,7]
startIndex = 190221
size = startIndex + 15
iterations = 0
while iterations < size:
    sumDig = recipes[fec] + recipes[sec]
    newRe = list(map(int,str(sumDig)))
    recipes += newRe
    
    fec = (1 + recipes[fec] + fec) % len(recipes) 
    sec = (1 + recipes[sec] + sec) % len(recipes)

    iterations += 1
    
print(''.join(map(str,recipes[startIndex:startIndex + 10])))  

# part 2 
fec = 0
sec = 1
recipes = [3,7]
find = False  
puzzle = list(map(int,str(190221)))
length = len(puzzle)
while not find:
    sumDig = recipes[fec] + recipes[sec]
    newRe = list(map(int,str(sumDig)))
    recipes += newRe
    
    fec = (1 + recipes[fec] + fec) % len(recipes) 
    sec = (1 + recipes[sec] + sec) % len(recipes)

    #print(len(recipes))
    if len(recipes) > length :
        if recipes[-length: ] == puzzle :
            print("index: ", len(recipes) - length)
            find = True
        if recipes[-length-1:-1] == puzzle:
            print("index: ", len(recipes) - length-1)
            find = True