#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:18:39 2017

@author: jonathan
"""


import matplotlib.pyplot as plt
import numpy as np


def MA(x, windowSize = 4, kind = 'mean'):
    """
    Uses a moving average to fill in missing values
    x: an univariate time series
    windowSize: how many observations to look foward and back
    kind: what method should be used?
        Options: mean, median, min,
                max, sum
    """
    funs = {'mean':np.nanmean, 'median':np.nanmedian, 
            'min':np.nanmin, 'max':np.nanmax, 
            'sum':np.nansum}
    func = funs[kind]
    k = windowSize
    missing = np.isnan(x)
    where = np.where(missing)
    for i in np.nditer(where):
        #print(type(i), i)
        vals = x[(i-k):(i+k)]
        #print(vals)
        impute = func(vals)
        #print(impute)
        x[i] = impute
    return x
    

