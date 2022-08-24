'''
isPalindrome() 함수는 약간 투 포인터 느낌으로 이해하면 편하다.
start와 end라는 파라미터를 받는데
각각은 중심에 1씩 서로 가까워 진다.
팰린드롬은 문자열을 반으로 접었을 때 값이 서로 같으면 팰린드롬이라고 할 수 있다.

그리고 이 코드에는 살짝의 스킬(?)이 들어가는데
c라는 리스트를 만들어 사용하는걸 볼 수 있다.
그런데 0번쨰만 사용하는 이유는 c라는 변수를 사용하고 함수내에서 값을 더하면
c변수를 지역변수로 간주해서 에러가 발생함(local val)
하지만 리스트는 참조하여 [0]을 보는것이기 때문에 문제가 발생하지 않음( id보세용)
'''
from sys import stdin
input = stdin.readline
def isPalindrome(string, start, end):
    c[0] += 1
    if start >= end: return 1
    elif string[start] != string[end]: return 0
    else: return isPalindrome(string, start+1, end-1)

for i in range(int(input())):
    c = [0]
    t = input().rstrip()
    print(isPalindrome(t, 0, len(t)-1), c[0])