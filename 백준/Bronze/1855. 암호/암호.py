n,t=int(input()),input()
lst=[val[::-1]if idx%2 else val for idx, val in enumerate([t[i:i+n]for i in range(0,len(t),n)])]
for i in range(n):
    for j in range(len(lst)):print(lst[j][i],end="")