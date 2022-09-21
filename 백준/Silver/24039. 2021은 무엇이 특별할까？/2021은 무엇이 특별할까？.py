def prime_number_sieve_sqrt(n): #소수 판별기 : O(sqrt(N))
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i]==0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst))

m = 100001
lst = prime_number_sieve_sqrt(m)
n = int(input())
for i in range(m-1):
    if n<lst[i]*lst[i+1]:
        print(lst[i]*lst[i+1])
        break
