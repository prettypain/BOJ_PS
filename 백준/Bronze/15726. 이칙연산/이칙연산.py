a,b,c = map(int, input().split())
print(int(a*b/c if a*b/c > a/b*c else a/b*c))