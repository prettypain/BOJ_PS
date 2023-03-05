n = int(input())
pn = "IOI" + "OI"*(n-1)
lpn = len(pn)

str_len = int(input())
s = input()
c= 0
for i in range(str_len-lpn+1):
    if s[i:lpn+i] == pn: c+=1
print(c)