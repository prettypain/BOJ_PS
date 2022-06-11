n = int(input())
if n%2==0:
    a = "* "*(n//2)
    b = " *"*(n//2)
else:
    a = "* "*(round(n/2+0.001))
    b = " *"*(int(n/2))
for i in range(n):
    print(a)
    print(b)
