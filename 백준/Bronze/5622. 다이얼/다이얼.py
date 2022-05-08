res = 0
for i in input():
    if i in "ABC":res+=3
    elif i in "DEF":res+=4
    elif i in "GHI":res+=5
    elif i in "JKL":res+=6
    elif i in "MNO":res+=7
    elif i in "PQRS":res+=8
    elif i in "TUV":res+=9
    elif i in "WXYZ":res+=10
    elif i in "0":res+=11
print(res)