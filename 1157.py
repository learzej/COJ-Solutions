# 1157 - u Calculate e
# http://coj.uci.cu/24h/problem.xhtml?pid=1157

from math import factorial

e = 0

print "n e"
print "- -----------"

for n in range(10):
    e += 1.0/factorial(n)
    d = str(e).split(".")[1]
    if int(d) != 0:
        if len(d) > 9:
            print n, "%.9f" % e
        else:
            print n, e
    else:
        print n, int(e)
