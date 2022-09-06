'''
이 문제는 쉽게 생각하면 쉽다(문제를 이해했다는 가정하에 진행한다)
먼저 k보다 커지게 되는 지점을 찾아야한다(단 i<=j)
k보다 커지는 [i, j]구간을 찾았다면
거기서 j+1해보자 그래도 k보다 크다를 만족한다.
입력되는 수는항상 1이상이라서 j를 늘려주면 값또한 늘어난다
즉 k < sum([i, j])를 만족하는 지점에서 뒤에 남은 값의 개수만큼 더 만족한다.
이 부분을 잘 캐치하면 문제를 쉽게 해결할 수 있다.

중요 포인터! : k < sum([i, j])를 만족한 지점이후 부터는 계속해서 만족한다.
이유 : 입력되는 숫자는 항상 100,000보다 크지 않은 자연수임이 보장되기 떄문.
고로 k < sum([i, j])를 만족한 순간 그 뒤에 남은 개수를 모두 더해주면 된다(n을 사용해서)

어떄유 참 웰논하쥬?(나만 모르는 웰논 ㅜ)
'''
from sys import stdin
input = stdin.readline
n = int(input())
lst = list(map(int, input().split()))
k = int(input())

start = 0
end = 0
c = 0
while end < n:
    s = sum(lst[start:end+1])
    if s>k:
        c += (n-end)
        start += 1
    elif end!=n and s<=k:
        end += 1
    else:
        start += 1
print(c)
