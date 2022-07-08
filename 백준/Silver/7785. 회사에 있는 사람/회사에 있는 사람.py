'''
이 문제의 핵심은 맵핑(딕셔너리)을 할 수 있는지 없는지 이다.
배열(리스트)로 해결하려고 하면 시간초과가 발생하므로 맵핑을 해야한다.
(또는 다른 빠른 자료구조를 사용하거나)
'''
import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    name, command = input().split()
    if command == "enter":
        dic[name] = 0
    else:
        dic.pop(name)
print('\n'.join(reversed(sorted(dic.keys()))))