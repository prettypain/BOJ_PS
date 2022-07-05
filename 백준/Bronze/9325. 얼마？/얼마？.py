for i in range(int(input())):
    res = int(input())
    for j in range(int(input())):
        a,b = map(int, input().split())
        res+= a*b
    print(res)
