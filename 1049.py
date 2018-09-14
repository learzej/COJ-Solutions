# 1049 - Sum
# http://coj.uci.cu/24h/problem.xhtml?pid=1049

n = int(raw_input())

if n >= 0:
    s = (n*(n+1))/2
    print s
else:
    s = (((n*-1)*((n*-1)+1)/2)*-1)+1
    print s
