t = input()
res = ""
c = 0
l = len(t)
for i in range(l):
    if t[i] =="." or i+1==l:
        c+= (1 if t[i] == "X" else 0)
        res += "AAAA"*(c//4) + "BB"*((c%4)//2) + ("." if t[i]=="." else "")
        c = 0
    elif t[i] == "X":
        c+=1
print(res if l==len(res) else -1)