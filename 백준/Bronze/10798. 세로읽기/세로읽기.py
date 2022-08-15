lst = [input() for i in range(5)]
ml = max(map(len, lst))
res = ""
for i in range(ml):
    for j in range(5):
        if len(lst[j])-1 < i:
            continue
        res += lst[j][i]
print(res)