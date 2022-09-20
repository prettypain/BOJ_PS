def is_prime(n):#소수 판별
    '''
    *@param {int} n 소수 판별 대상
    *@returns {bool} 소수인지
    *@TC : O(sqrt(N))
    '''
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True
for i in range(int(input())):
    t = int(input())
    while True:
        if is_prime(t): break
        t+=1
    print(t)
