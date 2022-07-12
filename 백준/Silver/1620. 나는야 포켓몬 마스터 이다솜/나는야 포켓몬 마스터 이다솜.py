import sys
I = sys.stdin.readline
n,m = map(int, I().split()) #포켓몬수, 문제 수
dic = {}
dic1 = {}
for i in range(1,n+1):
    t = I().strip()
    dic[i] = t
    dic1[t] = i
for i in range(m):
    t = I().strip()
    print(dic[int(t)] if t.isdigit() else dic1[t])