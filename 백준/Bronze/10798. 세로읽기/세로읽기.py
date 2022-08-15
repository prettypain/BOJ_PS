'''
가로로 지나가는 와중에 해당 행의 길이가 탐색하는 열의 번호+1보다 작은 경우만
패스해주고 나머진 전부 res에 저장하면 성공
'''
from sys import stdin
lst = [stdin.readline().rstrip() for i in range(5)]
ml = max(map(len, lst))
res = ""
for i in range(ml):
    for j in range(5):
        if len(lst[j])-1 < i:
            continue
        res += lst[j][i]
print(res)