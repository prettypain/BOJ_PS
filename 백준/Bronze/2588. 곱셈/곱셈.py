List = []
a = int(input())
b = input()[::-1]
s = 0
for i,v in enumerate(b):
    v = int(v)
    res = a*v*10**i
    s += res
    res = str(res)
    print(res[:len(res)-i])
print(s)
