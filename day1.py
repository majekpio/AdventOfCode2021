# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:30:22 2021

@author: Piotr Majek
"""

import numpy as np

file = 'day1_data.txt'

data = np.genfromtxt(file)

def day1_task1(data):
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1
    return count

def day1_task2(data):
    count = 0
    for i in range(len(data) - 3):
        sum_bot = data[i] + data[i + 1] + data[i + 2]
        sum_top = data[i + 1] + data[i + 2] + data[i + 3]
        
        if sum_top > sum_bot:
            count += 1
            
    return count
