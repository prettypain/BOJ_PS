import sys
import heapq

print = sys.stdout.write
input = sys.stdin.readline
q = []
for i in range(int(input())):
    x = int(input())
    if x>0:
        heapq.heappush(q, x)
    elif x==0:
        if len(q): print(f'{heapq.heappop(q)}\n')
        else: print('0\n')