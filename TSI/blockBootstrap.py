#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:45:37 2017

@author: jonathan
"""

import numpy as np


def blockBootstrap(x, b = 4, samples=1000, func=None):
    """
    Block Bootstrapping function
    x: a numpy array
    b: length of blocks
    samples: number of blocks to sample
    
    blockBoostrap is intended to produce samples of time series, but can
    also be used to create samples of statistics. 
    Simply pass a function to `func`
    """
    n = len(x)
    diff = n - (b+1)
    blocks = {}
    z = int(n/b)
    for i in range(diff):
        block = x[i:(b+i)]
        blocks[i] = block
    ind = np.random.randint(low = 0, high = diff, size=samples)
    samples = [blocks[i] for i in ind]
    samples = np.array(samples)
    r = samples.shape[0]
    ## diff = r - z
    results = []
    for i in range((r-z)):
        temp = samples[i:(z+i),:]
        if i < 5:
            print temp
        j,k = temp.shape
        temp = temp.reshape((j*k,))
        results.append(temp)
        if i < 5:
            print temp
    results = np.array(results) ## turns list of arrays to martrix
    if func:
        results = map(func, results)
    return results




def naBoot(x, windowSize = 4, samples = 1000):
    """
    Uses block bootstrapping to calculate imputation values
    """
    k = windowSize
    missing = np.isnan(x)
    where = np.where(missing)
    tsSamples = blockBootstrap(x)
    for i in np.nditer(where):
        vals = [row[(i-k):(i+k)] for row in tsSamples]
        est = [np.nanmean(y) for y in vals]
        print type(est), est
        x[i] = np.mean(est)
    return x


## test 1:
vals = range(20)
n = len(vals)
b = 4
diff = n - (b+1)
z = int(n/b)
for i in range(diff):
    block = vals[i:(b+i)]
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
    
    

