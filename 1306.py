# 1306 - Div 4
# http://coj.uci.cu/24h/problem.xhtml?pid=1306

import string

t = int(raw_input())

if t >= 1 and t <= 100:
    for i in range(t):
        s = raw_input()
        if len(s) < 100:
            if len(s) > 2:
                n = int(s[-2:])
                if n % 4 == 0:
                    print "YES"
                else:
                    print "NO"
            else:
                n = int(s)
                if n % 4 == 0:
                    print "YES"
                else:
                    print "NO"

