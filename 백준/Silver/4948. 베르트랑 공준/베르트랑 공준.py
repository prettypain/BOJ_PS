'''
이 문제의 핵심은 n+1~2*n 까지의 소수를 모두 찾는 것이다.
에라스토테네스의 체를 통해 n*2까지 구한 후
거기서 n+1이후부터의 소수만 개수를 체크해 출력하면 된다.

'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
def sieve(n):
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst[t+1:]))

while(t:=int(input()))!=0:
    print(f'{len(sieve(t*2))}\n')