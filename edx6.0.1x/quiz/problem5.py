def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sumOfProduct = 0
    i = 0
    for ele in listA:
        sumOfProduct += ele*listB[i]
        i += 1
    return sumOfProduct