# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:01:46 2022

@author: Vishnu Kadiyala
"""

import os

f = open('standings.txt', 'r')

content = f.read()

print('leader' + content[30: 42])