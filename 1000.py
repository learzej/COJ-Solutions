# 1000 - A+B Problem
# http://coj.uci.cu/24h/problem.xhtml?pid=1000

import string

if __name__ == "__main__":
    s = raw_input()
    ns = map(int, s.split())
    a = ns[0]
    b = ns[1]
    if a >= 0 and a <= 10:
        if b >= 0 and b <= 10:
            c = a + b
            print c
