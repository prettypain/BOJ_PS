c = [0,0]
n,m = map(int ,input().split())
List = [list(input()) for i in range(n)]
for i in List:
    if i.count("X")==0:
        c[0]+=1
for i in range(m):
    tmp = ""
    for j in range(n):
        tmp += List[j][i]
    if tmp.count("X")==0:
        c[1]+=1

print(max(c[0],c[1]))
