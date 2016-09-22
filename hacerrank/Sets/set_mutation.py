'''
Created on Aug 23, 2016

@author: inssharma027
'''

n = int(raw_input().strip())
if n > 0 and n < 1000:
    s = raw_input().strip()
    s = set(list(map(int, s.split(" "))))
    N = int(raw_input().strip())
    
    if N > 0 and N < 100:
        for i in xrange(N):
            cmdStr = raw_input().strip()
            cmdStr = cmdStr.split(" ")

            cmd = cmdStr[0]
            setLen = int(cmdStr[1])

            if setLen > 0 and setLen < 100:
                os = raw_input().strip()
                os = set(list(map(int, os.split(" "))))

                if cmd == "intersection_update":
                    s.intersection_update(os)
                elif cmd == "symmetric_difference_update":
                    s.symmetric_difference_update(os)
                elif cmd == "difference_update":
                    s.difference_update(os)
                elif cmd == "update":
                    s.update(os)
    print s
    print sum(s)