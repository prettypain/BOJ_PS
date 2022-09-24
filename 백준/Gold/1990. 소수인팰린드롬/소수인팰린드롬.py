'''
이 문제는 팰린드롬이면서 소수인 수를 찾는 문제이다.
그런데 수가 커질 수록 소수인지를 구하기가 힘들다.
그래서 첫 시도에는 MLE(메모리 초과)를 받았다.
메모리 초과를 해결하기 위해서 방법을 찾다가 이상한 규칙을 찾았다.
약 1천만부터 1억까지는 팰린드롬이면서 소수가 없었기 때문이다.
그렇다면 만약 1억이라는 입력이 들어왔을 때 1천만까지만 구하게 코드를
수정하면 괜찮을 것 같은데? 라고 생각해 바로 수정해 AC(정답)을 받았다.


첫 골드 문제에 희열은 굉장히 즐거웠다(학교에서ㅋㅋ)


tmi : 거의 내 힘으로 맞은 첫 골드문제...힝

'''
from sys import stdout
print = stdout.write
def is_pil(n):
    n = str(n); l = len(n)
    return n[:l//2] == n[l//2 +(1 if l%2 else 0):][::-1]

def sieve(n): #에라토스테네스의 체 함수 : O(sqrt(N))
    lst = list(range(n+1))
    lst[1] = 0
    for i in range(2, int(n**0.5)+1):
        if lst[i] == 0: continue
        for j in range(i+i, n+1, i): lst[j] = 0
    return list(filter(lambda x : x!=0, lst[a:]))

a,b = map(int, input().split())
b = min(b, 10000000)
for i in sieve(b):
    if is_pil(i):
        print(f'{i}\n')
print(f'{-1}')
