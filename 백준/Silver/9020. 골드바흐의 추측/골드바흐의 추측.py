
import sys
input = sys.stdin.readline
print = sys.stdout.write
t = 10001
primes = list(range(t)); primes[1] = 0

for i in range(2, int(t**0.5)+1):
    if primes[i]==0: continue
    for j in range(i+i, t, i): primes[j] = 0


for _ in range(int(input())):
    n = int(input())
    lst = primes[:n+1]
    half = n//2
    for i in range(half):
        if primes[half - i] and primes[half + i]:
            res = [primes[half - i], primes[half + i]]
            break
    print(f'{res[0]} {res[1]}\n')