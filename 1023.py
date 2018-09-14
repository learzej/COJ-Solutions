# 1023 - Financial Management
# http://coj.uci.cu/24h/problem.xhtml?pid=1023

s = 0
for i in range(12):
    n = float(raw_input())
    s += n
s /= 12
print "$"+str(s)
