import sys
input = sys.stdin.readline
for i in range(int(input())):
    tmp = list(map(int ,input().split()))
    avg = sum(tmp[1:])/tmp[0]
    c = len(list((filter(lambda x : x>avg, tmp[1:]))))
    print(f"{c/tmp[0]*100:.3f}%")