# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:58:20 2022

@author: zakha
"""

from enum import Enum
import ProgrammingLanguage

class Typization(Enum):
    strict = 1
    dynamic = 2

class LanguageFunctional(ProgrammingLanguage.ProgrammingLanguage):
    def __init__(self, name, year, mentions, typizition, lazy):
        super().__init__(name, year, mentions)
        self.typizition = typizition
        self.lazy = lazy
        
    def out(self):
        print("_____________________________\n" +
              "I'm Functional language\n" +
              "My characteristics is:\n" +
              "Name: " + self.name + '\n' +
              "Year: " + self.year +'\n' +
              "Years past: " + str(self.numberOfYears()) + '\n' +
              "Mentions: " + self.mentions +'\n' +
              "Typization: " + self.typizition.name + '\n' +
              "Do I have lazy calculations?: " + str(self.lazy) + '\n' +
              '_____________________________\n')