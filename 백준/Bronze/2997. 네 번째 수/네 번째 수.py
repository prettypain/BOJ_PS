lst = sorted(map(int, input().split()))
a,b = lst[1]-lst[0], lst[2]-lst[1]
if lst[0]+a==lst[1] and lst[1]+a==lst[2]:
    print(lst[2]+a)
elif lst[0]+b==lst[1] and lst[1]+b==lst[2]:
    print(lst[2]+b)
else:
    if lst[0]+a*2 == lst[1]:
        print(lst[0]+a)
    elif lst[1]+a*2 == lst[2]:
        print(lst[1]+a)
    elif lst[0]+b*2 == lst[1]:
        print(lst[0]+b)
    elif lst[1]+b*2 == lst[2]:
        print(lst[1]+b)