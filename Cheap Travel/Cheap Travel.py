try:
    A = list(map(int, input().split()))
    n = A[0]
    m = A[1]
    a = A[2]
    b = A[3]
    if b/m >= a:
        print(a*n)
    else:
        split_num = str(n/m).split('.')
        int_part = int(split_num[0])
        cost = b*int_part
        remain = (n%m)*a
        if remain > b:
            print(cost + b)
        else:
            print(cost+remain)
except:
    pass