'''
X를 카운트 하면서 마지막 또는 .을 만나면 카운트 했던 것에 해당하는 만큼
A 또는 B를 채운다 이때 사전순으로 먼저 오는 것을 답으로 하라고 했으니
A를 먼저 채운다(또한 A의 개수는 4개, B의 개수는 2개 즉 b(개수)는 A(개수)의 약수이다)
이점만 주의해서 풀면 쉽게 풀린다.
'''
from sys import stdin
t = stdin.readline().rstrip()
res = ""
c = 0
l = len(t)
for i in range(l):
    if t[i] =="." or i+1==l:
        c+= (1 if t[i] == "X" else 0)
        res += "AAAA"*(c//4) + "BB"*((c%4)//2) + ("." if t[i]=="." else "")
        c = 0
    elif t[i] == "X":
        c+=1
print(res if l==len(res) else -1)