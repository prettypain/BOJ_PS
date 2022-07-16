for i in range(int(input())):
    c = 0
    n = int(input())
    lst = sorted(map(int, input().split()))
    print((max(lst)-min(lst))*2)