n = int(input())
plus = 1
minus = 1
lst = list(map(int, input().split()))
before = lst[0]
res = []
if n==1:res.append(before)
for i in lst[1:]:
    if before <= i:
        plus += 1
        res.append(minus)
        minus = 1
    elif before >= i:
        minus += 1
        res.append(plus)
        plus = 1
    before = i
res.append(max(plus,minus))

before = lst[-1]
plus = 1
minus = 1
for i in lst[-2::-1]:
    if before <= i:
        plus += 1
        res.append(minus)
        minus = 1
    elif before >= i:
        minus += 1
        res.append(plus)
        plus = 1
    before = i
res.append(max(plus,minus))
print(max(res))