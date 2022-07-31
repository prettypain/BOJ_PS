'''
아주 간단한 문제이다.
그냥 주어진 수만큼 출력한다.
'''
from sys import stdin
I=stdin.readline
print("\n".join(map(lambda x:x*"=",[int(I().strip())for i in range(int(I().strip()))])))