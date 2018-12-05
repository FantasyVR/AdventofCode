# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:56:30 2018

@author: HV
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
            
                 
                