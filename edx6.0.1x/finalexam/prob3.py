def dict_invert(d):
    keys = d.keys()
    values = d.values()
    newDict = {}
    i = 0
    for value in values:
        if value not in newDict.keys():
            valList = []
        valList.append(keys[i])
        newDict[value] = valList
        newDict[value].sort()
        i = i + 1
    return newDict
    
print dict_invert({30000: 30, 600: 30, 2: 10})