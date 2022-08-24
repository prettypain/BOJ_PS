'''
솔직히 진법 변환할줄 몰라서 머리를 싸매고 하다가 실패해서 그냥 진법변환함수만
긁어왔다... ㅠ(솔루션)

f()함수는 n을 2~10진법으로 만든 리스트를 리턴해줌

is_palindrome()함수는 재귀버전으로 구현한 팰린드롬 판별기임
약간 투 포인터 느낌이 나는 방법임
양 끝부터 시작해 천천히 중앙으로 오는 방법임

나머지는 그냥 m진법으로 변환한 n이 팰린드롬이면 출력하고
출력이 하나도 없으면 NIE출력
'''
def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def f(n):
    lst = []
    for i in range(2, 10):
        lst.append(solution(n, i))
    return lst + [str(n)]

def is_palindrome(target, start, end): #팰린드롬 판별기 재귀버전
    return True if start >= end else (is_palindrome(target, start+1, end-1) if target[start]==target[end] else False)

from sys import stdin
input = stdin.readline
arr = f(int(input()))
c = 0
for idx, val in enumerate(arr):
    if is_palindrome(val, 0, len(val)-1):
        print(idx+2, val)
        c = 1
if not c:print("NIE")