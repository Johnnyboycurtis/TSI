#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:00:53 2017

@author: jonathan
"""

import numpy as np



def diff(x, n=1):
    s = x
    for i in range(n):
        s = s[:-1] - s[1:]
    return s
        