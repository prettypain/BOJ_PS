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
def is_palindrome(target, start, end):
    return True if start >= end else (is_palindrome(target, start+1, end-1) if target[start]==target[end] else False)
arr = f(int(input()))
c = 0
for idx, val in enumerate(arr):
    if is_palindrome(val, 0, len(val)-1):
        print(idx+2, val)
        c = 1
if not c:print("NIE")