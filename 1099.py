# 1099 - Pythagorean Numbers
# http://coj.uci.cu/24h/problem.xhtml?pid=1099

import itertools

while True:
    c = raw_input()
    ns = map(int, c.split())
    if len(ns) == 1 and ns[0] == 0:
        break
    else:
        a = ns[0]
        b = ns[1]
        c = ns[2]
        if a < 10000 and b < 10000 and c < 10000:
            ns = list(itertools.permutations(ns))
            f = False
            for x in ns:
                a = x[0]**2
                b = x[1]**2
                c = x[2]**2
                if c == a + b:
                    f = True
                    break
            if f:
                print "right"
            else:
                print "wrong"
