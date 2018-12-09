# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 21:37:57 2018

@author: RV
"""
import requests



def main():
    print("start downloading...")
#    if len(sys.argv) > 2:
#        print("not right args")
    address = "https://adventofcode.com/2018/day/"
    day = 8
    address += str(day) + "/input"
    
    r = requests.get(address)
    filename = "day"+str(day)+".txt"
    open(filename,"wb").write(r.content)
    print(filename)
    
if __name__ == "__main__":
    main()
    
