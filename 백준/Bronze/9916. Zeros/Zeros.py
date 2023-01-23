n = int(input())
for i in range(2, n): n*=i
print(str(n).count("0"))