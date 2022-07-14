import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m = -1
    for i in range(int(input())):
        name, al = input().split()
        al = int(al)
        if al > m:
            m = al
            n = name
    print(n)