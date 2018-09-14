# 3375 - Naebbirac Phrases
# http://coj.uci.cu/24h/problem.xhtml?pid=3375

t = int(raw_input())

if t >= 1 and t <= 100:
    for i in range(t):
        cadena = raw_input().split()
        c = 0
        for x, y in zip(cadena[0], cadena[1]):
            if not x == y:
                c += 1
        print c
