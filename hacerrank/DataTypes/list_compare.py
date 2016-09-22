'''
Created on Aug 15, 2016

@author: Shiv Sharma
'''
x = int(raw_input().strip())
y = int(raw_input().strip())
z = int(raw_input().strip())

l = int(raw_input().strip())
print [ [m,n,o] for m in xrange(x+1) for n in xrange(y+1) for o in xrange(z+1) if m+n+o != l]

# li = []
# for m in xrange(x+1):
#     for n in xrange(y+1):
#         for o in xrange(z+1):
#             if m+n+o < l:
#                 li.append([m,n,o])
#             
# print li

