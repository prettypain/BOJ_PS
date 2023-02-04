n = str(int(input())*int(input())*int(input()))
print(*[n.count(str(i)) for i in range(10)],sep="\n")