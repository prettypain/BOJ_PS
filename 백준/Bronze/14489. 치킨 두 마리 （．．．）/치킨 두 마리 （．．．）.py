a,b = map(int, input().split())
p = int(input())
t = a+b-p*2
print(a+b if t<0 else t)