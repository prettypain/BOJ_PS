'''
이 문제는 비트 마스킹 문제지만
입력되는 수의 범위가 1~20이라서 20짜리 배열만들어서
i = lst[i-1]로 인지하고 풀면 된다.
즉 1~20을 인덱스이자 값으로 사용한다.
'''
from sys import stdin
lst = [0]*20
for i in range(int(stdin.readline())):
    command = stdin.readline().rstrip()
    if command == "all":       lst = [1]*20
    elif command == "empty":  lst = [0]*20
    else:
        command, target = command.split()
        target = int(target)
        if command == "add":lst[target-1] = 1
        elif command == 'remove':lst[target-1] = 0
        elif command == "check":print(lst[target-1])
        elif command == "toggle":lst[target-1] = 0 if lst[target-1] else 1