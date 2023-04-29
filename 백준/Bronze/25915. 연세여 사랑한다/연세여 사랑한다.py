dis = 0
on = input()
for i in "ILOVEYONSEI":
    dis += abs(ord(i)-ord(on))
    on = i
print(dis)