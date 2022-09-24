m = 7380000
lst = [True]*m
lst[1] = False
lst[0] = False
pb = True

for i in range(2, int(m**0.5)+1):
    if lst[i] == 0: continue
    for j in range(i+i, m, i): lst[j] = False
print([i for i in range(2, m) if lst[i]][int(input())-1])