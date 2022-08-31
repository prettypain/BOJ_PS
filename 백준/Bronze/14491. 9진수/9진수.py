n =int(input())
i = 0
while True:
    if n<9**i:
        break
    i+=1
if i<=1:
    t = n
else:
    t = ""
    for k in range(i-1, -1, -1): #i = 2 : 1, 0
        for j in range(1, 10):
            if j*9**k>n:
                t += str(j-1)
                if n==0: break
                n%= (j-1)*9**k
                break
print(t)