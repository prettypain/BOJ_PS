for t in range(int(input())):
    input()
    n = int(input())
    print("YES" if sum([int(input()) for _ in range(n)])%n==0 else "NO")