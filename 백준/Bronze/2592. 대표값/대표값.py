'''
이 문제 같은 경우 입력되는 숫자의 범위가 작아서
갯수 카운팅을 리스트 형태로 했다.
인덱스는 해당 수를 나타내고 그 인덱스에 있는 값이 카운트 횟수다.
'''
import sys
input = sys.stdin.readline
List = [0]*1001
s = 0

for _ in range(10):
    n = int(input())
    List[n]+=1
    s+=n
print(f'{int(s/10)}\n{List.index(max(List))}')
