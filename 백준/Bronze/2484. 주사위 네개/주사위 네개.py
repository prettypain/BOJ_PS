m = 0
for i in range(int(input())):
    s = 0
    a,b,c,d = map(int, input().split())
    lst = [a,b,c,d]
    if a==b==c==d: s += (50000 + a*5000)
    elif lst.count(a)==3 or lst.count(b)==3: s+= 10000 + 1000*(a if lst.count(a)==3 else b)
    
    elif a==b and c==d: s += 2000 + 500*a + 500*c
    elif a==c and b==d: s += 2000 + 500*a + 500*b
    elif a==d and c==b: s += 2000 + 500*a + 500*b
    
    elif a==b or d==a or a==c: s+= 1000 + 100*a
    elif b==c or b==d: s+= 1000 + 100*b
    elif c==d: s+= 1000 + 100*c
    else: s+= max(lst)*100
    if s>m: m = s
print(m)