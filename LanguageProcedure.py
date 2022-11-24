# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:48:10 2022

@author: zakha
"""

import pickle
import ProgrammingLanguage

class LanguageProcedure(ProgrammingLanguage.ProgrammingLanguage):
    def __init__(self,name, year, hasAbstractTypes):
        super().__init__(name, year)
        self.hasAbstractTypes = hasAbstractTypes
        
    def out(self):
        print("_____________________________\n" +
              "I'm Procedure language\n" +
              "My characteristics is:\n" +
              "Name: " + self.name + '\n' +
              "Year: " + self.year +'\n' +
              "Do I have abstract types?: " + str(self.hasAbstractTypes) + '\n'
              '_____________________________\n')
        