ab = [[0,0] for _ in range(26)]
for a in input():ab[ord(a)-97][0]+=1
for b in input():ab[ord(b)-97][1]+=1
print(sum([i[0]-(m:=min(i))+i[1]-m for i in ab]))