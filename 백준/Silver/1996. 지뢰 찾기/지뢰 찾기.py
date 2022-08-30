'''
문제를 해결할 수 있는 방법을 생각하는건 간단하지만 구현이 조금 귀찮다.
x, y가 좌표 범위를 탈출하는지 지켜봐야 하고 반복문 더 쓰면 시간 초과가 발생할 것
같아서 깡구현...

모든 좌표에 가보고 각 좌표에 상, 하, 좌, 우, 4개의 대각선칸이 숫자면 그 값들을 모아서
10이상이면 M으로 tmp에 추가하고 아니면 모은 값으로 추가하면 끝
'''
from sys import stdin
input = stdin.readline
def f(x,y):
    if x<0 or x>=n or y<0 or y>=n: return False
    return int(arr[x][y]) if arr[x][y].isdigit() else 0
n = int(input())
arr = [list(input().rstrip()) for i in range(n)]
res = []
for x in range(n):
    tmp = ""
    for y in range(n):
        if arr[x][y].isdigit(): 
            tmp += "*"
        else:
            t=f(x-1, y-1)+f(x-1, y)+f(x-1, y+1) + f(x, y-1)+f(x, y)+f(x, y+1) + f(x+1, y-1)+f(x+1, y)+f(x+1, y+1)
            tmp += "M" if t>9 else str(t)
    res.append(tmp)
for i in res: print(i)