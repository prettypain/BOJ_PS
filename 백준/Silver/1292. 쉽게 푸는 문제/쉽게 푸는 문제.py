"""
이 문제는 입력이 3 7일 때
3334444555556666667777777
를 모두 더하는 것이 아니라
12 (23334) 4445555
까지 더하는 문제 이다.
아쉽게도 나는 겁나 단순무식하게 해본다.
"""
List= []
a,b = map(int, input().split())
for i in range(1,1001):
    for j in range(i):
        List.append(i)
print(sum(List[a-1:b]))
