def is_pil(n):
    n = str(n); l = len(n)
    return n[:l//2] == n[l//2 +(1 if l%2 else 0):][::-1]
def is_prime(n):#소수 판별
    '''
    *@param {int} n 소수 판별 대상
    *@returns {bool} 소수인지
    *@TC : O(sqrt(N))

    <증명>
    자연수에서 두 개 이상의 소수의 곱으로 이루어져 있는 수, 1과 소수를 제외한 수를 합성수라고 합니다.
    어떤 수가 합성수가 아님을 판별하면 그 수는 소수입니다.
    자연수 N을 N = P X Q (P <= Q, P 와 Q 는 1과 N이 아닌 자연수)을 만족하는 합성수라고 가정했을 때
    N = P X Q >= Q x Q = Q ^ 2
    -> Q <= sqrt(N)

    따라서 N은 sqrt(N)보다 작은 적어도 하나의 인수를 가지므로 sqrt(N)까지만 나누어보면 됩니다.
    '''
    if n==1 or (n!=2 and n%2==0): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0: return False
    return True

m = 1000001
lst = [True]*m
lst[1] = False
lst[0] = False
pb = True
for i in range(2, int(m**0.5)+1):
    if lst[i] == 0: continue
    for j in range(i+i, m, i): lst[j] = False

for i in range(int(input()), m):
    if lst[i] and is_pil(i):
        print(i)
        pb = False
        break

if pb: print(1003001) #m까지의 수중에서 찾지 못했다면 그다음 필름이면서 소수인 수를 출력


'''
def check_inter(target):
    target = str(target)
    for i in range(1, len(target)):
        if not is_prime(int(target[:-i])): return False
    return True

lst = []
N = int(input())
for i in range(10**(N-1), 10**N+1):
    if is_prime(i) and check_inter(i):
        lst.append(i)
'''
