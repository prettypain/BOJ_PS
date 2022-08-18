n = int(input())
if n==0:
    print("divide by zero")
else:
    lst = list(map(int, input().split()))
    l = len(lst)
    ex = sum(map(lambda x : x*lst.count(x)/l, set(lst)))
    print(f'{sum(lst)/n/ex:.2f}')