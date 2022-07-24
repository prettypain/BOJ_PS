'''
이 문제의 핵심은
'거대한 좌표평면에 비해 사람은 작은 존재이므로, 편의상 각 사람의 크기는 무시하자.'
라는 문구에 있다.
즉 사과 자체가 사람이 있는 좌표에 닫지 않는 이상 닫는 것이라고 할 수없다.
반지름이 아무리 커도 사과는 (x, r)에 있을 것이고 x축에 닫는 표면은 x좌표 단 하나뿐이다.
문제 자체가 쓸대 없는 정보를 많이 줘서 애드훅 냄새가 난다..(킁킁)
'''
from sys import stdin
input = stdin.readline
lst = list(map(int, input().split()))
tar = int(input().split()[0])
print(lst.index(tar)+1 if tar in lst else 0)