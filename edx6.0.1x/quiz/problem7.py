def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    resultDict1 = {}
    resultDict2 = {}
    d1diff = list(set(d1.keys()) - set(d2.keys()))
    d2diff = list(set(d2.keys()) - set(d1.keys()))
    d1d2intersect = list(set(d1.keys()) & set(d2.keys()))
    
    for key1 in d1diff:
        resultDict2[key1] = d1[key1]
    for key2 in d2diff:
        resultDict2[key2] = d2[key2]
    for key in d1d2intersect:
        resultDict1[key] = f(d1[key], d2[key])
        
    return (resultDict1, resultDict2)
    
def f(a,b):
    if a > b:
        return a > b
    else:
        return a + b
    
print dict_interdiff({0: 0, 2: 5, 5: 2}, {0: 0, 2: 5})