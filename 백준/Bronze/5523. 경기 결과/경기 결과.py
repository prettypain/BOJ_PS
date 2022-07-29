from sys import stdin
input = stdin.readline
c = [0, 0, 0]
for i in range(int(input())):
    a,b = map(int, input().rstrip().split())
    c[0 if a>b else 1 if b>a else 2] += 1
print(" ".join(map(str, c[:2])))