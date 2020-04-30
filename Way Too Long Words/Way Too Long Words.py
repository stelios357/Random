for _ in range(int(input())):
    www = input()
    if len(www) > 10:
        print(www[0] + str(len(www)-2) + www[-1])
    else:
        print(www)