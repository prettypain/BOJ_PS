a,b = map(int, input().split())
t = set(map(int, input().split())) - set(map(int, input().split()))
l=len(t)
print(f'{l}\n{" ".join(map(str,sorted(list(t))))}' if l else l)