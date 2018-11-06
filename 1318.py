# 1318 - Abc
# http://coj.uci.cu/24h/problem.xhtml?pid=1318

c = raw_input()
n = map(int, c.split())

if n[0] <= 100 and n[1] <= 100 and n[2] <= 100:
    letras = raw_input()
    a = min(n)
    n.remove(a)
    c = max(n)
    n.remove(c)
    b = n[0]
    p = 0
    for i in letras:
        if i == 'A':
            print a,
        elif i == 'B':
            print b,
        elif i == 'C':
            print c,
