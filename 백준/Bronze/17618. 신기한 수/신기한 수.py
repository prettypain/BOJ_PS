n = int(input())+1
lst = [0]*n
for i in range(1,n):
    if i%sum(map(int, str(i)))==0: lst[i] = 1
print(sum(lst[:n]))