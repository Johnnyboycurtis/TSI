
def rollingWindow(x, windowSize = 5, function = sum):
    """
    Rolling window function to compute any rolling means, medians, etc
    x = should be an array or list
    windowSize = defaults to 5
    function = whatever function you want to calculate that returns an int/float
                defaults to sum for a rolling sum
    """
    n = len(x)
    j = windowSize
    diff = n - j
    results = [] 
    for i in xrange(0, diff):
        data = x[i:(j+i)]
        results.append( function(data) )
    return results
    




def rollingMean(x, windowSize = 3):
    """
    x should be a list or an array of values
    windowSize is the length of values to look back; default to 3
    """
    n = len(x) 
    j =  windowSize
    diff = n - j ## difference in length
    results = []
    for i in xrange(0, diff):
        data = x[i:(j+i)]
        mean = sum(data) * 1.0 / j
        results.append(mean)
    return np.array(results)





