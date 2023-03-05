n = int(input())
lst = []
for i in range(6):
    for j in range(6):
        if i+j==n and not sorted([i,j]) in lst:
            lst.append(sorted([i,j]))
print(len(lst))
