'''
와.....1시간 넘게 불태웠따...
솔직히 소인수 분해 뺴고는 구현하는데 10분걸렸다...
소인수 분해 제작하는데 10분....
소인수 분해 최적화하고 하는데 30분...


정식 명칭 : 에라스토테네스의 체
에라토스테네스의 체는 sqrt(n)까지 검사해도 문제 없다.
(시간 복잡도가 O(N)에서 -->  O(sqrt(N))으로 개선 가능) sqrt는 루트
요거 보면 이해 쌉가능 : https://blog.kakaocdn.net/dn/t8DvJ/btqPFUxKua7/Ssy29y1KDH1PmkDEbwK1C1/img.gif

설명:
    2~n의 소수를 구한다고 가정할 때
    2~n까지 반복하면서 소수를 만나면 그 소수의 배수를 제거한다.
    이걸 n-2회 반복하면 완성이다.
    10을 예롤 들자.
    [1,2,3,4,5,6,7,8,9,10] 이있다.
    1은 소수가 아니니까 제거
    [2,3,4,5,6,7,8,9,10]
    2는 소수다, 그럼 2의 배수를 모두 제거한다.
    [2,3,5,7,9] 2의 배수 제거 과정에서 4, 6, 10이 제거 되었다(제거된 수는 모두 소수가 아님)
    3을 만난다 그(녀)는 소수다. 그(녀)의 배수를 모두 제거한다.
    [2,3,5,7] 3의 배수 제거 과정에서 9가 죽었다(?)
    5를 만났다. 그(녀)는 소수지만 더이상 10이하의 소수는 없다. 즉 넘어가준다.
    7을 만났다. 그(녀)는 소수지만 더이상 10이하의 소수는 없다. 또 넘어가준다.
    더이상 아무것도 남지 않았다.
    이제 살아남은자(소수)들을 돌려보내 주자.



소인수 분해 코드 설명:
    1 x 16 = 16
    2 x 8 = 16
    4 x 4 = 16
    8 x 2 = 16
    16 x 1 = 16
    2 x 8 = 16 은 8 x 2 = 16 과 대칭이다.
    즉, 가운데 약수를 기준으로 해서 각 등식이 대칭적인 형태를 보이기 때문에
    우리는 특정한 자연수 N이 소수인지 확인하기 위해 바로 가운데 약수까지만
    '나누어떨어지는지' 확인하면 된다.
    위의 예시에서는 가운데 약수가 4이기때문에 2부터 4까지만 확인하면 된다.
    다시 말해 제곱근(가운데 약수)까지만 확인하면 된다.
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write
def sieve(start, end):
    lst = list(range(end+1))
    lst[1] = 0
    for i in range(2, int(end**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, end+1, i): lst[j] = 0
    return lst
def factorization(x):
    val = []
    d = 2
    sqx = int(x**0.5)+1
    while d <= sqx:
        if x % d == 0:
            val.append(d)
            x = x / d
        else:
            d = d + 1
    if x > 1: val.append(x)
    return val

res = 0
a,b = map(int, input().split())
prime = sieve(0, b)
for i in range(a, b+1):
    if prime[i]: continue #소수라면 제외
    if prime[len(factorization(i))]: res+=1
print(f'{res}')