import math
t = int(input())
while(s:=input())!='=':
    if s.isdigit():
        t = math.trunc(eval(str(t)+sym+s))
    else: sym = s
print(t)