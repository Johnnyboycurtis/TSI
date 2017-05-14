#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:45:37 2017

@author: jonathan
"""

import numpy as np
import matplotlib.pyplot as plt


def blockBootstrap(x, b = 4, seriesSamples=10, func=None):
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
    nBlocks = (n/b) + 1 ## calculate how many blocks will it take to create 
    ## one series; we add one extra block at the end
    blockSamples = nBlocks*seriesSamples ## then calculate how many blocks are needed
    ## to create however many samples are requested
    diff = n - (b+1)
    blocks = {}
    #z = int(n/b)
    for i in range(diff):
        block = x[i:(b+i)]
        blocks[i] = block
    ind = np.random.randint(low = 0, high = diff, size=blockSamples)
    samples = [blocks[i] for i in ind]
    samples = np.array(samples)
    ## diff = r - z
    results = []

    for i in range(seriesSamples): #range((r-nBlocks)):
        temp = samples[i:(nBlocks+i),:]
        if i < 3: ## debugging
            print i, temp ## debugging
        j,k = temp.shape
        temp = temp.reshape((j*k,))
        temp = temp[:n]
        results.append(temp)
        if i < 3: ## debugging
            print i, temp
    results = np.array(results) ## turns list of arrays to martrix
    if func:
        results = map(func, results)
    return results










def naBoot(x, windowSize = 4, samples = 1000):
    """
    Uses block bootstrapping to calculate imputation values
    
    x: a numpy array of values with missing values
    windowSize: window size for block bootstrap sampling
    samples: how many bootstrapped time series should be used for imputation?
    
    returns an a complete time series as a numpy array
    """
    k = windowSize
    missing = np.isnan(x)
    where = np.where(missing)
    tsSamples = blockBootstrap(x, windowSize, samples)
    for i in np.nditer(where):
        vals = [row[(i-k):(i+k)] for row in tsSamples]
        est = [np.nanmean(y) for y in vals]
        print type(est), est
        x[i] = np.mean(est)
    return x















