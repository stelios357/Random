try:
    A = list(map(int, input().split()))
    x1 = A[0]
    y1 = A[1]
    x2 = A[2]
    y2 = A[3]
    if x1 == x2 or y1 == y2:
        if x1 == x2:
            dist = y2-y1
            print(x1+dist, y1 , x2+dist, y2)
        if y1 == y2:
            dist = x2 - x1
            print(x1, y1 + dist, x2, y2 + dist)
    else:
        dist1 = x1-x2
        dist2 = y1-y2
        if abs(dist1) == abs(dist2):
            print(x1,y2,x2,y1)
        else:
            print("-1")
except:
    pass