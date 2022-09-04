from sys import stdin
lst = [0]*20
stdin.readline
for i in range(int(stdin.readline())):
    command = stdin.readline().rstrip()
    if command.count(" "):
        command, target = command.split()
        target = int(target)
    if command == "add":
        lst[target-1] = 1
    elif command == "remove":
        lst[target-1] = 0
    elif command == "check":
        print(lst[target-1])
    elif command == "toggle":
        lst[target-1] = 0 if lst[target-1] else 1
    elif command == "all":
        lst = [1]*20
    elif command == "empty":
        lst = [0]*20