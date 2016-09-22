'''
Created on Nov 16, 2015

@author: Shiv Sharma
'''

# def simpleArraySum(arr):
#     arraySum = 0
#     for element in arr:
#         arraySum = arraySum + int(element)
#     
#     return arraySum
# 
# n = int(input())
# algorithms = input()
# numlist = algorithms.split()
# print(simpleArraySum(numlist[:n]))

#===============================================================================
# def veryLargeSum(largeArray):
#     largeArraySum = 0
#     for element in largeArray:
#         largeArraySum = largeArraySum + int(element)
#     return largeArraySum
#  
# limit = int(input())
# count = 0
# li = []
# for x in input().split():
#     if count == limit - 1:
#         break
#     li.append(int(x))
#  
# print(veryLargeSum(li))
#===============================================================================


def diagonalDifference(lst, rowsCount):
    diagonalSum1 = 0
    diagonalSum2 = 0
    diagonalElementIndex1 = 0
    diagonalElementIndex2 = rowsCount-1
    for idx, item in enumerate(li):
        if item in li[:idx]:
            idx = idx
        else:
            idx = li.index(item)
        if idx == diagonalElementIndex1 and idx <= len(lst):
            diagonalElementIndex1 += rowsCount + 1
            diagonalSum1 += item
 
        if idx == diagonalElementIndex2 and idx <= len(lst) - rowsCount:
            diagonalElementIndex2 += rowsCount - 1
            diagonalSum2 += item
    return abs(diagonalSum1 - diagonalSum2)
li = []
rowCount = int(input())
numRow = rowCount
while rowCount > 0:
    row = input()
    rowElementList = row.split()
    rowElementList = rowElementList[:numRow]
    for x in rowElementList:
        li.append(int(x))
    rowCount = rowCount - 1
print(diagonalDifference(li, numRow))




