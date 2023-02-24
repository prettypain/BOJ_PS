import sys
def prime_number_sieve_sqrt(n): #O(sqrt(N))
    '''
    *@param {int} n 범위의 끝(2부터)
    *@return {list} 2~n까지의 소수
    *@TC : O(nloglogn)

    요거 보면 이해 쌉가능 : https://blog.kakaocdn.net/dn/t8DvJ/btqPFUxKua7/Ssy29y1KDH1PmkDEbwK1C1/img.gif

    원래 에라토스테네스의 체는 2~n까지 검사해 O(N)의 시간복잡도를 가진다.
    하지만 이 함수는 2~sqrt(N)까지 검사해 O(sqrt(N))의 시간 복잡도를 가진다.
    여기 부터는 증명의 내용이 담겨있다.
    
    n 이하의 모든 소수를 구한다고 해보자.
    이 때 해당 수 n은 자연수 a, b에 대해 n = a * b 라고 표현할 수 있다.
    예를들어 12는 2*6 혹은 3*4 등으로 나타낼 수 있다. a, b가 자연수라는 부분이 중요하다.
    또 m = sqrt(n) 이라고 하면 n = m * m 이라고 할 수 있다.

    n = a*b이고, n = m*m 이라 했으므로 a*b = m*m 이다. (a,b는 자연수이고 m은 n의 제곱근)
    그럼 이 상태에서 a랑 b가 자연수가 되려면 다음의 세가지 경우 중 하나만 가능하다.
        1. a=m 이고 b=m (n이 4와 같은 경우라서 m도 2처럼 자연수라면 가능하다.)
        2. a<m 이고 b>m
        3. a>m 이고 b<m

    a, b가 자연수가 되려면 항상 위의 세가지 중 하나가 되고,
    그렇다면 min(a, b) <= m 인것을 알 수 있다. (a와 b 중 작은 것은 m보다 작거나 같다.)
    
     즉, n의 모든 약수에 해당하는 a와 b가 어떠한 약수이더라도 둘 중 하나는 무조건 m(=sqrt(n)) 이하 이므로,
     m까지만 조사한다면 n이 소수인지 알 수 있게 되는 것이다.

     그럼 이건 정확히 n에만 국한된 것이지, n 이하의 모든 수에 대해 만족하진 않는다고 생각할 수 있다.
     하지만 n보다 작은 것 중 가장 큰 수인 n-1만 해도 sqrt(n)>sqrt(n-1) 이다.
     즉 n보다 작은 수는 모두 sqrt(n) 내에 포함되므로 n 뿐만 아니라
     n 미만의 모든 값에 대해 소수 판정이 가능하다.
     '''
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i]==0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst))

arr = prime_number_sieve_sqrt(1000000)[::-1]
for _ in range(int(sys.stdin.readline())):
    pb = True
    n = int(sys.stdin.readline())
    for i in arr:
        if n%i==0:
            pb = False
            break
    sys.stdout.write(("YES" if pb else "NO") + "\n")