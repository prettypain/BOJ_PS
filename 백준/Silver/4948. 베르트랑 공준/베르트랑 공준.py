'''

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
