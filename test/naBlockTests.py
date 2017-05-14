#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:06:49 2017

@author: jonathan
"""

import numpy as np
import matplotlib.pyplot as plt


## tests for block bootstrap and naBoot

## test 1:
vals = range(20)
n = len(vals)
b = 3
diff = n - (b+1)
z = int(n/b)
Blocks = []
for i in range(diff):
    block = vals[i:(b+i)]
    Blocks.append(block)
    print i,block

out = blockBootstrap(vals)

r = out.shape[0]


results = []
for i in range((r-z)):
    temp = out[i:(z+i),:]
    print temp
    j,k = temp.shape
    temp = temp.reshape((j*k,))
    results.append(temp)
    print temp
    if i == 5:
        break


vals
temp = np.array(range(20)) * 1.0
temp[4] = np.nan
temp[10] = np.nan

test = naBoot(temp)
    
    



## test 2:
s = np.random.randn(20).cumsum()
test = s.copy()
test[4] = np.nan
test[15:17] = np.nan
plt.plot(s)
plt.plot(test)



hopefultest = naBoot(test)


