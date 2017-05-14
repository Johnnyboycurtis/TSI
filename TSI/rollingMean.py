## rolling window functions

import numpy as np


def smoothingWindow(x, backward = 2, forward = 2, function = sum):
    """
    Rolling window which smooths a time series
    The function to compute any rolling means, medians, etc using 
        back and forward values.
    Unlike a cummulative window function, this function uses future values
        from current i-th value
    x: should be an numpy array or list
    windowSize: defaults to 5
    function: whatever function you want to calculate that returns an int/float
                defaults to sum for a rolling sum
    """
    n = len(x)
    j = backward
    k = forward
    results = []
    for i in xrange(n):
        start = i-j
        end = i+k
        while start < 0:
            start += 1
        data = x[(start):(end)]
        results.append( function(data) )
    return results
    




def cumMean(x, windowSize = 3):
    """
    x should be a list or an array of values
    windowSize is the length of values to look back; default to 3
    """
    n = len(x) 
    j =  windowSize
    results = []
    for i in xrange(n):
        temp = j
        while (i-j) < 0:
            
        data = x[:i]
        if len(data) > j:
            data = data[:j]
        mean = sum(data) * 1.0 / j
        results.append(mean)
    return np.array(results)





