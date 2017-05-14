#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:28:09 2017

@author: jonathan
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.available
plt.style.use('ggplot')



df = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))
csdf = df.cumsum()


df.plot()

## test 1:
ax = csdf.plot()
ax.set_xlabel("time")
ax.set_ylabel("value")
ax.set_title("Time Series")


## test 2:
mat = np.random.randn(1000, 4)
plt.plot(mat)



def plotTS(vals, xlabel="time", ylabel="values", title="Time Series", xlim=None, ylim=None):
    if isinstance(vals, pd.Series) or isinstance(vals, pd.DataFrame):
        vals = pd.DataFrame(vals)
    ax = vals.plot()
    ax.set_xlabel("time")
    ax.set_ylabel("value")
    ax.set_title("Time Series")
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    return ax
    
    
        







