# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:47:43 2022

@author: zakha
"""

from abc import ABC, abstractmethod

class ProgrammingLanguage(ABC):
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    @abstractmethod
    def out(self):
        pass
         