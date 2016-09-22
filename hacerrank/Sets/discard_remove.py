'''
Created on Aug 23, 2016

@author: inssharma027
'''
n = int(raw_input().strip())
if n > 0 and n < 20:
    s = raw_input().strip()
    s = set([int(x) for x in s.split(" ")][:n])
    #print s

N = int(raw_input().strip())
if N > 0 and N < 20:
    cmds = []

    for i in xrange(N):
        cmd = raw_input().strip()
        cmds.append(cmd)

    for cmd in cmds:
        cmdArgs = cmd.split() 
        #print cmdArgs   
        liCmd = cmdArgs.pop(0)
        if len(cmdArgs) == 0:
            if liCmd == 'pop':
                s.pop()
        elif len(cmdArgs) == 1:
            if liCmd == 'discard':
                s.discard(int(cmdArgs[0]))
            elif liCmd == 'remove':
                s.remove(int(cmdArgs[0]))
    print sum(s)