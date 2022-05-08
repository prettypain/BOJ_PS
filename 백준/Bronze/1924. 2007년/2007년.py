def month(mon):
    if mon in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mon in [4, 6, 9, 11]:
        return 30
    return 28
dic = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 0: 'SUN'}

m,d = map(int, input().split())
for i in range(1,m):
    d+= month(i)
print(dic[d%7])