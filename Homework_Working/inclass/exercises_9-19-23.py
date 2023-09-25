# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:25:54 2023

@author: claire 
"""

import numpy as np

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
c = np.zeros(len(a))

for i in range(7):
    c[i] = max((a[i]), b[i])
    print(c)

