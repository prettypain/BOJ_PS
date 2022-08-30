'''
문제를 해결할 수 있는 방법을 생각하는건 간단하지만 구현이 조금 귀찮다.
x, y가 좌표 범위를 탈출하는지 지켜봐야 하고 반복문 더 쓰면 시간 초과 오질것 같아서
그냥 깡구현해서 n**4구현은 면했다..ㅎ

모든 좌표에 가보고 각 좌표에 상, 하, 좌, 우, 4개의 대각선칸이 "*"인지 검사해 보고 개수를
카운트 해서 현재 내 위치에 값으로 대입하면 된다.
'''
from sys import stdin
input = stdin.readline
def f(x,y):
    if x<0 or x>=r or y<0 or y>=c: return False #각 위치가 0~r-1, 0~c-1을 벗어나는지 체크
    return arr[x][y]=="*" #x,y위치에 폭탄이 있는지
while True:
    r,c = map(int, input().split())
    if r==0 or c==0: break
    arr = [list(input().rstrip()) for i in range(r)]
    res = []
    for x in range(r):
        tmp = ""
        for y in range(c):
            if arr[x][y] == "*": 
                tmp += arr[x][y]
            else:
                tmp += str(f(x-1, y-1)+f(x-1, y)+f(x-1, y+1) + f(x, y-1)+f(x, y)+f(x, y+1) + f(x+1, y-1)+f(x+1, y)+f(x+1, y+1))
        res.append(tmp)
    for i in res: print(i)