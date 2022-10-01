n = int(input())
lst = [0]
for i in sorted(map(int, input().split())): lst.append(lst[-1]+i)
print(sum(lst))