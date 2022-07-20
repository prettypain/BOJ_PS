'''
문제를 이해했다는 가정하에 설명

이 문제의 핵심이라고 할 수 있는 부분은
for문이다, 내가 ps한 방법은
lst(바뀔 수 있는 리스트), arr(바뀔 수 없는 리스트)라고 할 때
먼저 arr의 가장 큰 값의 인덱스 번호에 lst의 가장 작은 값을 배치한다.
그리고 이미 위 과정을 거친 값들은 제외한다.
이 방식대로 풀면 문제가 풀리지만
난 lst를 정렬하고(그럼 작은값부터 순서대로 있음) tar에다가 arr의 값을 복사해주고
(리스트의 경우 그냥 =대입연사자 쓰면 값복사가 아니라 주소복사가 되므로 copy사용을 권장)
새로운 리스트를 만들어 풀었다.
세세한 설명은 주석을 달겠다.
'''
import sys
input = sys.stdin.readline
n = int(input())
res = [0]*n #이 리스트가 최종 결과 리스트이다.
lst = sorted(map(int, input().split()))
arr = list(map(int, input().split()))
tar = arr.copy()
for i in range(n):
    idx = tar.index(max(tar)) #바뀔 수 없는 리스트에서 가장 큰 값의 인덱스를 찾아
    res[idx] = lst.pop(0) # 그 인덱스에 위치한 값을 바뀔 수 있는 리스트의 값중 가장 작은 값으로 대입
    tar[idx] = -1 #이후 바뀔 수 없는 리스트이 가장 큰 값의 위치한 값을 제외(삭제해버리면 인덱스 문제)
print(sum(map(lambda x,y : x*y, res,arr))) #최종적으로 곱하면 완