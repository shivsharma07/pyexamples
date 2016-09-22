'''
Created on Aug 29, 2016

@author: Shiv Sharma
'''
#Variable A contains a set of items.
#Variable N tells the program how many sets will be created.

A = set(map(int, raw_input().split()))
N = int(raw_input())

#List in which we will store different sets once we create them.

set_list = []

#We loop N times and variable x creates N sets. We append these sets to a list. Previously created variable set_list now contains a number of different sets.

for i in range(N):
    x = set(map(int, raw_input().split()))
    set_list.append(x)

#Default value of the resuls variable is True

result = True

#We iterate over differnet sets in a list.  Result will stay True, unless we find a set to whom A is not a superset.

for i in set_list:
    if not A.issuperset(i):
        result = False

print result