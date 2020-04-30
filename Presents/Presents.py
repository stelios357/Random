n = int(input())
dict = {}

A = list(map(int, input().split()))
for i in range(n):
    dict[i] = A[i]
key_list = list(dict.keys())
val_list = list(dict.values())

for j in range(n):
    print(key_list[val_list.index(j+1)]+1 , end = " ")
#4
#2 3 4 1
