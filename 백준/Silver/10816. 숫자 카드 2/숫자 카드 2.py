#https://hongcoding.tistory.com/12
'''
음 암만봐도 이분탐색으론 힘들어 보인다...
파이썬 내장함수 bisect를 이용해 배열에서 타겟이 있는 가장 왼쪽 인덱스와 오른쪽 인덱스를
구해서 오른쪽 인덱스 - 왼쪽인덱스를통해 타겟의 총 갯수를 알 수 있다.
물론 정렬이 되어있어야 한다.
결론 함수짱.
'''
import sys
from bisect import bisect_left, bisect_right
def f(arr, tar):
    return bisect_right(arr,tar)-bisect_left(arr, tar)
input = sys.stdin.readline
input()
List = sorted(map(int, input().split()))
input()
for i in list(map(int, input().split())):
    print(f(List, i),end=" ")
