#https://docs.python.org/3/library/collections.html#collections.deque
import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for i in range(1,n+1): queue.append(i)
while len(queue)!=1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])