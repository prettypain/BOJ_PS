'''
그저 문자열을 순차적으로 3개씩 탐색하면서 그것이 JOI인 경우와 IOI인 경우
카운팅 하면 끝.
'''
from sys import stdin
n = stdin.readline().rstrip()
jc = 0
ic = 0
for i in range(len(n)-2):
    if n[i:i+3] == "JOI": jc += 1
    elif n[i:i+3] == "IOI": ic += 1
print(f'{jc}\n{ic}')
