'''
솔직히 tle날줄 알았는데 생각보다 빨랐다.
일단 내 풀이는 입력받은 n이 소수일때까지 +1해주고 소수이면 그때 출력한다.
이게 끝이고 이 코드의 핵심은 is_prime()함수다.
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
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

for i in range(int(input())):
    t = int(input())
    while not is_prime(t):
        t+=1
    print(f'{t}\n')