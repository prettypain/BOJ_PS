s = input().lower()
lst = []
while True:
    try:
        a = input()
        lst += a.split()
    except:
        break
c = 0
for i in lst:
    if s in i: c+=1
print(c)