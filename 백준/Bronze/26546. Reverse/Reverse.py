for _ in range(int(input())):
    t,a,b = input().split()
    a,b = int(a),int(b)
    t = list(t)
    t[a:b] = []
    print(*t,sep="")