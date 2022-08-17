'''
생각보다 간단하다.
그냥 x, y 범위가 주어졌을 때 그 범위만큼 2차원 배열에 +1 해주고
최종적으로 m보다 높은 값만 카운팅 해준다(m 이하인 경우 보이기 떄문)
원래 이렇게 반복문이 많으면 별로 좋지 못하다.
(시간이 오래 걸리니까)
하지만 이 문제는 테스트 케이스를 적게 주어지므로 이렇게 단순하게 풀어도 정답 처리.
'''
from sys import stdin
input = stdin.readline
lst = [[0 for j in range(100)] for i in range(100)]
n, m = map(int, input().split())
for _ in range(n):
    bx, by, tx,ty = map(int, input().split())
    for x in range(bx-1, tx):
        for y in range(by-1, ty):
            lst[x][y] += 1
c = 0
for i in range(100):
    for j in range(100):
        if lst[i][j]>m:
            c+=1
print(c)