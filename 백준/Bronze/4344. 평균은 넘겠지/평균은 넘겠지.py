import sys
input = sys.stdin.readline
for i in range(int(input())):
    tmp = list(map(int ,input().split()))
    avg = sum(tmp[1:])/tmp[0]
    c = 0
    for i in tmp[1:]:
        if i>avg: c+=1
    print(f"{c/tmp[0]*100:.3f}%")
