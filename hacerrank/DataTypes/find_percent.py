'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''
N = int(raw_input().strip())
studentList = []
if N >= 2 and N <= 10:
    for i in xrange(N):
        student = raw_input().strip()
        studentList.append(student.split())
name = raw_input().strip()

studentDict = {}
for stud in studentList:
    studentDict[stud.pop(0)] = stud

sum = 0.0
for marks in studentDict[name]:
    sum = sum + float(marks)
print "%.2f" % round(float(sum/3.0), 2)