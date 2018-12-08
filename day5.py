# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:56:30 2018

@author: RV
"""
# part 1
"""
polymer = open("day5.txt").read()
reaction = True
while(reaction):
    length = len(polymer)
    for i in range(len(polymer)-1):
        if(abs(ord(polymer[i]) - ord(polymer[i+1])) == 32 ):
            if(i+2 < length):
                polymer = polymer[:i] + polymer[i+2:]
            else:
                polymer = polymer[:i]
                break
            
    if(length == len(polymer)):
        reaction = False

print(len(polymer))
"""


#part 2
"""
import sys
polymers = open("day5.txt").read()
shortest = sys.maxsize
for index in range(65,91):
    char = chr(index)
    lchar = chr(index+32)
    polymer = polymers
    polymer = polymer.replace( char, "")
    polymer = polymer.replace(lchar, "")
    
    reaction = True
    while(reaction):
        length = len(polymer)
        for i in range(len(polymer)-1):
            if(abs(ord(polymer[i]) - ord(polymer[i+1])) == 32 ):
                if(i+2 < length):
                    polymer = polymer[:i] + polymer[i+2:]
                else:
                    polymer = polymer[:i]
                break
            
        if(length == len(polymer)):
            reaction = False
            
    if(shortest > len(polymer)):
        shortest = len(polymer)
    
print(shortest)
"""


# imporved method
"""
import sys
polymers = open("day5.txt").read()
shortest = sys.maxsize
for index in range(65,91):
    char = chr(index)
    lchar = chr(index+32)
    polymer = polymers
    polymer = polymer.replace( char, "")
    polymer = polymer.replace(lchar, "")
    
    reaction = True
    while(reaction):
        for i in range(len(polymer)-1):
            if polymer[i] == "*" or i+1 >= len(polymer):
                continue
            for atom in polymer[i+1:]:
                if atom == "*":
                    continue
                if(abs(ord(polymer[i]) - ord(atom)) == 32 ):
                    polymer[i]   = '*'
                    polymer[i+1] = '*'
                    
    polymer = polymer.replace('*',"")
    if(shortest > len(polymer)):
        shortest = len(polymer)
        
print(shortest)
"""

"""
总体思路，直接讲26种配对方式给找出来，然后利用str的replace函数将成对的消去，简单直接
Ref: https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4e5kl
"""
import time
# efficient way of part 1
line = open("day5.txt").read().splitlines()[0]

start = time.time()
oldline = None
while oldline != line:
    oldline = line
    for i in range(0,26):
        line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
        line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
end = time.time()
print("Part 1 time:", end-start)
print("Part1:")
print(len(line))         

# efficient way of part 2
original = line
best = len(line)
start = time.time()
for j in range(0,26):
    line = original
    line = line.replace(chr(ord("a") + j),"")
    line = line.replace(chr(ord("A") + j),"")
    oldline = None
    while oldline != line:
        oldline = line
        for i in range(0,26):
            line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

    best = len(line) if len(line) < best else best
    
end = time.time()
print("Part 1 time:", end-start)
print("Part2:")
print(best)
                 
"""
另一个思路：
相当于两个指针一直前进，如果发现了相同的就从str里pop出去。
Ref: https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4jzni
"""    
from string import *
def collapse(s):
    p = ['.']
    for u in s:
        v = p[-1]
        if v != u and v.lower() == u.lower():
            p.pop()
        else:
            p.append(u)
    return len(p) - 1


s = open('day5.txt').read().strip()
print(collapse(s))
print(min(collapse(c for c in s if c.lower() != x) for x in ascii_lowercase))    