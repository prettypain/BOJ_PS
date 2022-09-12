from sys import stdin
input = stdin.readline
#count는 중복 없는게 특징이라 보통 깡구현해서 문자열 탐색해왔는데
#이 문제는 중복제거라... 혹시 했는데..헐....이게 문제냐 처음이다 이런문제
print(input().rstrip().count(input().rstrip()))