import sys
def s(target):
    s = 0
    while target>0:
        s += target%10
        target//=10
    return s
n = int(sys.stdin.readline())+1
lst = [0]*n
for i in range(1,n):
    if i%s(i)==0: lst[i] = 1
sys.stdout.write(f'{sum(lst[:n])}')