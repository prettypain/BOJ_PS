'''
그냥 x,y 입력 받아서  (x-1, y-1) ~ (x+9, y+9)까지에 해당하는 위치를 모두 1로 바꿔서
최종적으로 합한 결과값을 출력하면 끝~
같은 곳이 여러번 입력에 해당되도 어자피 1로 고정이라 중복 문제 해결
'''
from sys import stdin
input = stdin.readline
lst = [[0 for j in range(100)] for i in range(100)]
n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            lst[i][j] = 1
print(sum(map(sum,lst)))
