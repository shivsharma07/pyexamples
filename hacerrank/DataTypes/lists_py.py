'''
Created on Aug 13, 2016

@author: Shiv Sharma
'''
N = int(raw_input().strip())
cmds = []

for i in xrange(N):
    cmd = raw_input().strip()
    cmds.append(cmd)
L = []
for cmd in cmds:
    cmdArgs = cmd.split()    
    liCmd = cmdArgs.pop(0)
    if len(cmdArgs) == 0:
        if liCmd == 'sort':
            L.sort()
        elif liCmd == 'reverse':
            L.reverse()
        elif liCmd == 'pop':
            L.pop()
        elif liCmd == 'print':
            print L
    elif len(cmdArgs) == 1:
        if liCmd == 'append':
            L.append(int(cmdArgs[0]))
        elif liCmd == 'remove':
            L.remove(int(cmdArgs[0]))
        elif liCmd == 'pop':
            L.pop(int(cmdArgs[0]))
        elif liCmd == 'index':
            L.index(int(cmdArgs[0]))
        elif liCmd == 'count':
            L.count(int(cmdArgs[0]))
    elif len(cmdArgs) == 2:
        if liCmd == 'insert':
            L.insert(int(cmdArgs[0]), int(cmdArgs[1]))
    else:
        print "invalid command"