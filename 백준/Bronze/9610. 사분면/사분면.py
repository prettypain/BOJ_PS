'''
예전에 사분면 판별기를 만들었던 기억이 나네요...힝, 그떈 순순했는데..
'''
import sys
input = sys.stdin.readline
arr = [0,0,0,0,0]
for _ in range(int(input())):
    x,y = map(int, input().split())
    if x==0 or y==0: arr[4] += 1
    elif x>0 and y>0: arr[0] += 1
    elif x<0 and y>0: arr[1] += 1
    elif x<0 and y<0: arr[2] += 1
    else: arr[3] += 1
for i in range(5):
    print('Q'+str(i+1)+':' if i!=4 else 'AXIS:', arr[i])