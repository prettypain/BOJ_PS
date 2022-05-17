n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
List = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        List[i][j] = arr[i][j] + tmp[j]

for i in List:
    for j in i:
        print(j,end=" ")
    print()
