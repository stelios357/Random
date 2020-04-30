import math

# 1 ≤ d ≤ 30, 0 ≤ sumTime ≤ 240
# 0 ≤ minTime i ≤ maxTime i ≤ 8
X = list(map(int, input().split()))
d = X[0]
h = X[1]
total_min = 0
total_max = 0
totalsh = 0
study = []
avg = h / d
avg_2 = 2 * avg
mini = []
maxi = []
ppp = []
fina = 0
for i in range(d):
    Y = list(map(int, input().split()))
    mini.append(Y[0])
    total_min += mini[i]
    maxi.append(Y[1])
    total_max += maxi[i]
if total_min - 1 < h < total_max + 1:
    print("YES")
    for i in range(d):
        if i == range(d):
            fina = h - totalsh
        else:
            sh = math.ceil((mini[i] + maxi[i]) / 2)
            ppp.append(sh)
            totalsh += sh
    if mini[d - 1] - 1 < fina < maxi[d - 1] + 1:
        print(ppp, end="")
        print(fina)
    else:
        while fina < mini[d - 1] - 1:
            while 1:
                pass
            pass
        pass
else:
    print("NO")
