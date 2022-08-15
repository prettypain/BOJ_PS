a,b = input().split()
lst = [] #차이 값 저장용
dif = len(b)-len(a)
for i in range(dif+1):
    t = " "*i + a + " "*(dif-i)
    res = ""
    for j in range(len(b)):
        if t[j] == " ": #문자를 채워야할 대상이라면
            res += b[j]
        else:
            res += t[j]

    #차이 계산 후 저장
    c = 0
    for j in range(len(b)):
        if res[j] != b[j]: c+=1
    lst.append(c)
print(min(lst))