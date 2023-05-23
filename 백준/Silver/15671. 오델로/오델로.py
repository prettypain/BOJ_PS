'''
시작하기 전에 흰돌이 (4, 4), (5, 5) 에
두 개 놓여져 있고, 검은돌이 (4, 5), (5, 4) 에 놓여져 있다고 가정한다.
또한 검은돌부터 게임을 시작한다.
(5, 4)는 리스트로 접근할 때 5번째 행에 4번째 요소로 해석할 수 있다. 즉 (y, x)

중요!
1. 내턴에 돌을 놓았을 때 바뀐 돌에 의해서 다른 돌은 영향받지 않는다.
2. 현재 놓은 위치에서 한방향으로 갔을 때 처음만난 같은팀 돌까지만 영향을 준다.


빈칸 : +(plus 기호)
흰돌 : O(대문자 o)
검돌 : X(대문자 x)

'''
def g():
    for i in graph:print(*i)
n = 6
is_in = lambda x,y : 0<=x<n and 0<=y<n

dxs = [-1, 0, +1, -1, +1, -1, 0, +1]
dys = [-1, -1, -1, 0, 0, +1, +1, +1]
#0 1 2
#3 - 4
#5 6 7

graph = [['+' for x in range(n)] for y in range(n)]
graph[2][2],graph[3][3],graph[2][3],graph[3][2] = 'OOXX'

now = 'X'
for i in range(int(input())):
    y,x = map(lambda x : int(x)-1, input().split())
    graph[y][x] = now
    now = 'O' if now=='X' else 'X'
    val = graph[y][x]
    temp = [x,y]
    
    for dx,dy in zip(dxs,dys):
        x,y = temp
        ping = []
        while True:
            x,y = dx+x, dy+y
            if not is_in(x,y) or graph[y][x]=="+":
                ping = []
                break
            if graph[y][x]==val: break
            
            ping.append((x,y))
        
        for xping, yping in ping:
            graph[yping][xping] = val
b,w = sum([i.count('X')for i in graph]),sum([i.count('O')for i in graph])
for i in graph:
    for j in i:
        print('B' if j=='X' else 'W' if j=='O' else '.',end="")
    print()

if b>w:
    print("Black")
else:
    print("White")
