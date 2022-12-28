#단순히 몫을 구하는 문제
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(sum(map(lambda x : int(x)//k, input().split())))