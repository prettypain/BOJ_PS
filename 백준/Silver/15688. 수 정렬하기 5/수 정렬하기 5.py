import sys
input = sys.stdin.readline
List = []
for i in range(int(input())):
    List.append(int(input()))
for i in sorted(List):
    print(i)
