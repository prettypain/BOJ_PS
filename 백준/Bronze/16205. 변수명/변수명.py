#1카멜 : camelCase
#2스네 : snake_case
#3파스 : PascalCase

t, s = input().split()
lst, tmp = [], ''
s+='0'
if t=='1':
    for i in s:
        if i=='0' or ord(i)<91:
            lst.append(tmp.lower())
            tmp = "" if i=='0' else i
        else: tmp+=i
    
elif t=='2':
    for i in s:
        if i=='0' or i=="_":
            lst.append(tmp.lower())
            tmp = ""
        else: tmp += i

else:
    tmp = s[0]
    for i in s[1:]:
        if i=='0' or ord(i)<91:
            lst.append(tmp.lower())
            tmp = "" if i=='0' else i
        else: tmp+=i

    
print(lst[0],end="")
for i in lst[1:]:print(i[0].upper()+i[1:],end="")
print()
for i in lst:print(i,end=("_" if lst[-1]!=i else ""))
print()
for i in lst:print(i[0].upper()+i[1:],end="")