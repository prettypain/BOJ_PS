n = int(input())
string = ""
for i in range(n):
    string += " "+input()
for i in [chr(j) for j in range(97, 123)]:
    string = string.replace(i, " ")
print(*sorted(map(int, string.split())), sep="\n")