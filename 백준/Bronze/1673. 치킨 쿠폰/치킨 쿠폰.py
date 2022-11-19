import sys
input = sys.stdin.readline
print = sys.stdout.write
while True:
    try:
        n, k = map(int, input().split())
        stamp = n #도장
        count = n  #치킨 먹은 횟수
        while stamp//k>0:
            t = stamp//k
            stamp = (stamp%k) + t
            count += t
        print(f'{count}\n')
    except:
        break