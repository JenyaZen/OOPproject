# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:53:14 2022

@author: zakha
"""
import pickle

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
   
class Container:
    def __init__(self):
      self.head = None
        
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    
    def showInfo(self):
        node = self.head
        while (node is not None):
            node.data.out()
            node = node.next
        print("There's no more objects in this container")
    
    def clear(self):
        self.head = None
        
    def openFromFile(self, file):
        self.head = None
        
        with open(file, 'rb') as f:
            opened_data = pickle.load(f)
        
        for i in opened_data:
            self.push(i)
        
    
    def saveToFile(self, file):
        saveData = []
        node = self.head
        while (node is not None):
            saveData.append(node.data)
            node = node.next
        
        with open(file, 'wb') as f:
            pickle.dump(saveData, f)
                