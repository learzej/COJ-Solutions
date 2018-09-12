# 1003 - General Election
# http://coj.uci.cu/24h/problem.xhtml?pid=1003

t = int(raw_input())

if t >= 1 and t <= 100:
    for e in range(t):
        s = raw_input()
        ns = map(int, s.split())
        if len(ns) == 2:
            n = ns[0]
            m = ns[1]
            if n >= 2 and n <= 5 and m >= 1 and m <= 100:
                votos = [0] * n
                c = True
                for i in range(m):
                    if c:
                        s = raw_input()
                        ns = map(int, s.split())
                        if len(ns) == n:
                            for x in range(len(ns)):
                                y = ns[x]
                                if y >= 0 and y <= 1000:
                                    votos[x] += y
                                else:
                                    c = False
                        else:
                            c = False
                    else:
                        break
                if c:
                    print votos.index(max(votos)) + 1
