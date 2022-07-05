import sys
s=[int(sys.stdin.readline()) for _ in range(8)]
ss=sorted(s,reverse=1)[:5]
print(sum(ss))
for i in sorted([s.index(i)+1 for i in ss]):print(i,end=" ")