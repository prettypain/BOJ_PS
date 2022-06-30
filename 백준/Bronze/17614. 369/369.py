c=0
for i in range(3,int(input())+1):
    i = str(i)
    c+= i.count('3') + i.count('6') + i.count('9')
print(c)