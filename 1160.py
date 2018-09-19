# 1160 - Number Steps
# http://coj.uci.cu/24h/problem.xhtml?pid=1160

N = int(raw_input())

for i in range(N):
    ns = map(int, raw_input().split())
    if all(x >= 0 and x <= 10000 for x in ns):
        x = ns[0]
        y = ns[1]
        if y >= (x - 2) and y <= x:
            if x % 2 == 0 and y % 2 == 0:
                print x + y
            elif x % 2 == 1 and y % 2 == 1:
                print ((x + y) - 1)
            else:
                print "No Number"
        else:
            print "No Number"
