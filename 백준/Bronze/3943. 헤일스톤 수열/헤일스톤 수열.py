import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    List = [n]
    while n!=1:
        if n%2==0: n//=2
        else: n=n*3+1
        List.append(n)
    print(max(List))