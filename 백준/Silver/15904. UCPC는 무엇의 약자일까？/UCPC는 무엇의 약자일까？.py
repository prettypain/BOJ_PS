u,c1,p,c2 = 0,0,0,0
for i in input():
    if i=="U" and not u:
        u = 1
    elif i=="C" and u and not c1:
        c1 = 1
    elif i=="P" and c1 and not p:
        p = 1
    elif i=="C" and p and not c2:
        c2 = 1
print(f'I {"love UCPC" if u and c1 and p and c2 else "hate UCPC"}')