#1<= n <= 1000
c = 0
n = int(input())
for i in range(1,n+1):
    if i<10:#한자리 수
        c+=1
    elif i<100:#두 자리수
        c+=1
    elif i<1000:#세 자리수 
        i = str(i)
        if int(i[1])+int(i[1])-int(i[0]) == int(i[2]):
            c+=1
    else: #네 자리
        i = str(i)
        if (int(i[1])+int(i[1])-int(i[0]) == int(i[2])) and (int(i[2])+int([1])-int(i[0])==int(i[3])):
            c+=1
        
print(c)
