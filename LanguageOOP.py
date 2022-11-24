# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:48:09 2022

@author: zakha
"""

from enum import Enum
import pickle
import ProgrammingLanguage

class Inheritance(Enum):
    single = 1
    multiple = 2
    interface = 3

class LanguageOOP(ProgrammingLanguage.ProgrammingLanguage):
    def __init__(self, name, year, mentions, inheritance):
        super().__init__(name, year, mentions)
        self.inheritance = inheritance
        
    def out(self):
        print("_____________________________\n" +
              "I'm OOP language\n" +
              "My characteristics is:\n" +
              "Name: " + self.name + '\n' +
              "Year: " + self.year +'\n' +
              "Years past: " + str(self.numberOfYears()) + '\n' +
              "Mentions: " + self.mentions +'\n' +
              "Type of inheritance: " + self.inheritance.name + '\n' +
              '_____________________________\n')
        