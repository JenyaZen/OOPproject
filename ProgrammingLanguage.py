# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:47:43 2022

@author: zakha
"""

from abc import ABC, abstractmethod

import datetime

currentYear = datetime.date.today().year

class ProgrammingLanguage(ABC):
    def __init__(self, name, year, mentions):
        self.name = name
        self.year = year
        self.mentions = mentions
        
    def numberOfYears(self):
        return currentYear - int(self.year)
    
    @abstractmethod
    def out(self):
        pass
         