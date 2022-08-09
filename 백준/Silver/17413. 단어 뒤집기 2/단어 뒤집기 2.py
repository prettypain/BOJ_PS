res = ""
tmp = ""
status = False #<>부등호 범위 in out 체크용
for i in input():
    if i=="<":
        status = True
        if len(tmp)>0:
            res += tmp[::-1]
            tmp = ""
    elif i==">":
        status = False
        res += ">"
        continue

    if status:
        res += i
    elif i==" ":
        res += tmp[::-1]+i
        tmp = ""
    else:
        tmp += i
print(res+tmp[::-1])