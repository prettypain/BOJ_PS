"""
내 랭크의 기준은 나보다 몸무게가 크면서 키도 큰 사람의 수 + 1이 내 랭크가 된다.
이점을 이용하면
나보다 큰(몸무계,키)사람의 수를 구해 그 수의 +1을 하면 그게 내 랭크가 된다.
"""
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
rank = []
for w,h in arr:
    c = 1
    for i in range(n):
        tar = arr[i]
        if tar[0] > w and tar[1] > h:
            c+=1
    rank.append(c)
for i in rank:
    print(i,end=" ")