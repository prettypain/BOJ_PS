for _ in range(int(input())):
    p, m = map(int, input().split())
    print(p-len(list({int(input()) for i in range(int(p))})))