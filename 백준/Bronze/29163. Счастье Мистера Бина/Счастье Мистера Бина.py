input()
t = [0,0]
for i in list(map(int, input().split())):
    if i%2==0: t[1] += 1
    else: t[0] += 1
print("Happy" if t[1]>t[0] else "Sad")