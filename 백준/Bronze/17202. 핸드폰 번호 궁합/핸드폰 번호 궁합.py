a = input()
b = input()
ab = ""
for i in range(8):ab+=a[i]+b[i]
while len(ab)!=2:
    t=""
    for i in range(len(ab)-1):
        t+= str(int(ab[i])+int(ab[i+1]))[-1]
    ab = t
print(ab)