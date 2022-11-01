lst = input().split()
n = int(lst.pop(0))
while n!=len(lst): lst += input().split()
print(*sorted(map(lambda x : int(x[::-1]), lst)), sep="\n")