def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    totalArea = 0
    while start < stop:
        startVal = f(start)
        totalArea += startVal * step
        start = start + step
    return totalArea
    
print round(f(5.0),3)
print radiationExposure(0, 5, 1)