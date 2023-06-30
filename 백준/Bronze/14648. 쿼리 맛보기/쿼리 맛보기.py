import sys
input = sys.stdin.readline
print = sys.stdout.write
n,q = map(int, input().split())
lst = list(map(int, input().split()))
for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        print(f'{sum(lst[t[1]-1:t[2]])}\n')
        lst[t[1]-1],lst[t[2]-1] = lst[t[2]-1],lst[t[1]-1]
    else:print(f'{sum(lst[t[1]-1:t[2]])-sum(lst[t[3]-1:t[4]])}\n')