# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:18:03 2018

@author: RV
"""
"""
Ref: https://www.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/ebepyc7
using deque is more faster than using blist and list

Time Consuming Comparasion:
    
- list:  >1 hour
- blist: 10 seconds
- deque: 0.015 seconds
"""

from collections import deque,defaultdict
import time

def marbalgame(numPlayers, lastMarbel):
    gameQue = deque([0])
    scores  = defaultdict(int)
    for marbelIndex in range(1, lastMarbel + 1):
        if marbelIndex % 23 == 0:
            gameQue.rotate(7)
            scores[marbelIndex % numPlayers] += gameQue.pop() + marbelIndex
            gameQue.rotate(-1)
        else:
            gameQue.rotate(-1)
            gameQue.append(marbelIndex)
            
    return max(scores.values()) if scores else 0
start = time.time()
highScore = marbalgame(476 ,71431 )
end = time.time()

print("High Score:",highScore)
print("Escaped time: ", end - start)