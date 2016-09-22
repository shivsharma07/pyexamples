'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''
str = raw_input().strip()
args = raw_input().strip()

argList = args.split(" ")
str = str[:int(argList[0])] + argList[1] + str[int(argList[0])+1:]
print str

#second solution
li = list(str)

li[int(argList[0])] = argList[1]
str = "".join(li)
print str

