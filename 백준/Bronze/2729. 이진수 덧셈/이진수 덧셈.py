import sys
input = sys.stdin.readline
for i in range(int(input())):
    a,b = input().split()
    print(bin(int(a,2) + int(b,2))[2:])
