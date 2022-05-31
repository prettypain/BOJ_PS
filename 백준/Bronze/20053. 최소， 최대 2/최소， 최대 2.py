import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    List = list(map(int, input().split()))
    MAX = List[0]
    MIN = List[0]
    for i in List:
        if i > MAX:
            MAX = i
        elif i < MIN:
            MIN = i
    print(MIN,MAX)
