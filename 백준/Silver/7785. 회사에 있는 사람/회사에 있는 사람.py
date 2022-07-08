n = int(input())
dic = {}
for i in range(n):
    name, command = input().split()
    if command == "enter":
        dic[name] = 0
    else:
        dic.pop(name)
print('\n'.join(reversed(sorted(dic.keys()))))
