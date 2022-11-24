# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:42:52 2022

@author: zakha
"""

import sys
from Container import Container
from LanguageOOP import LanguageOOP, Inheritance
from LanguageProcedure import LanguageProcedure
from LanguageFunctional import LanguageFunctional, Typization


print('Hello\n')
if (len(sys.argv) != 3):
    print('You need to give me input and output files!!\n')
    sys.exit()
    
print('Creating a container...\n')
container = Container()
print('Container created!\n')
print('Adding objects from ' + sys.argv[1] + ' to Container\n')
container.openFromFile(sys.argv[1])
print('Container filled!\n')
print('Hey, container, what you got?\n')
container.showInfo()
print('Now sorting...')
container.sortList()
print('What you got after sorting?')
container.showInfo()
print('Emptying container\n')
container.clear()
print('Container is now empty...\n')
print('Saving container to ' + sys.argv[2] + '\n')
container.saveToFile(sys.argv[2])
print('Container saved!\n')
print('Bye Bye!\n')

    
