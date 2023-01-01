t = input()
lst = input().split()
for i in lst: t=t.replace(i, i.lower())
print(t)