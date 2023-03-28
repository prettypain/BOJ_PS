n = int(input())
lst = list(map(int, input().split()))
s = lst[0]
if n>1:
    print(s,end=" ")
    for idx,val in enumerate(lst[1:]):
        t = val*(idx+2)-s
        print(t,end=" ")
        s+=t
else: print(s)