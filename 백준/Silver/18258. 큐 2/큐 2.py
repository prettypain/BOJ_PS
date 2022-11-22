#그냥 큐를 구현하라는데로 구현하면 된다. 또는 가져오거
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

q = deque()
for _ in range(int(input())):
    t = input().rstrip()

    
    if "pop" in t: print(f'{q.popleft() if len(q) else -1}\n')

    elif "size" in t: print(f'{len(q)}\n')

    elif "empty" in t: print(f'{1 if len(q)==0 else 0}\n')

    elif "front" in t: print(f'{-1 if len(q)==0 else q[0]}\n')

    elif "back" in t: print(f'{-1 if len(q)==0 else q[-1]}\n')

    else: q.append(t.split()[1])