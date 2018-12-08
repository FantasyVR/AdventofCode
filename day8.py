# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:05:07 2018

@author: RV
"""
"""
Tree Definition
"""    
class Tree(object):
    def __init__(self,numChild = 0, numMetaData = 1):
        self.numChild = numChild
        self.numMetaData = numMetaData
        self.children = []
        self.metaData = []
    
    def insertChild(self,node):
        self.children.append(node)
        
    def insertMetaData(self, metaData):
        self.metaData += metaData
        
    def getNumChildren(self):
        return self.numChild
    
    def getNumMetaData(self):
        return self.numMetaData
    
    def getChildren(self):
        return self.children
    
    def getMetaData(self):
        return self.metaData
 
"""
Create Tree from input data
"""
def createTree(data): 
    [numChild, numMetaData] = data[0:2]
    root = Tree(numChild, numMetaData)
    
    for i in range(numChild):
        node , tmpdata = createTree(data[2:])
        root.insertChild(node)
        data = data[:2] + tmpdata
        
    root.insertMetaData(data[2:2+numMetaData])
    data = data[2+numMetaData:]
    
    return root,data
    
"""
Traver the tree to get sum of all metadata entries
"""
def traverTree(tree):
    total = 0
    total += sum(tree.getMetaData())
    for i in range(tree.getNumChildren()):
        total += traverTree(tree.getChildren()[i])
    return total
  
"""
Traver the tree to get value of the root node
"""
def computeValueofRoot(tree):
    valueofNode = 0
    # if it's leaf node, compute the value from metadata and return
    if(tree.getNumChildren() == 0):
        valueofNode += sum(tree.getMetaData())
        return valueofNode

    metaData = tree.getMetaData()
    for index in metaData:
        if index <= tree.getNumChildren():
            child = tree.getChildren()[index-1]
            valueofNode += computeValueofRoot(child)
    
    return valueofNode

test = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
data =list(map(int, open("day8.txt","r").read().split(" ")))
#data = list(map(int,test.split(" ")))
root, data = createTree(data)
# part 1
print(traverTree(root))
# part 2
print(computeValueofRoot(root)) 