'''
s함수는 몫과 나머지를 이용해서 각 자리수의 합을 구했다.
그런데 for문에서 sum(map(int, str(i)))를 이용해서 합을 구했을 때는 두배 이상 느려졌다.
즉 문자로 처리하는 것은 편리하지만 속도는 느리다고 할 수 있다.
'''
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