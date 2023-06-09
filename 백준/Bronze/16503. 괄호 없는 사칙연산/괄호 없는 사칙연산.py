def f(s,a,b):return int(a+b if s=="+" else a-b if s=="-" else a*b if s=="*" else a/b)
a,b,c,d,e = map(lambda x : int(x) if x.isdigit() else x, input().split())
print(*sorted([f(d,f(b,a,c),e), f(b,a,f(d,c,e))]),sep="\n")