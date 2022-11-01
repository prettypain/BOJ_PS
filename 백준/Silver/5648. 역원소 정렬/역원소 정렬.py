'''
이 문제는 입력받는 방식이 귀찮을 뿐이지 문제 자체는 쉽다.
그냥 입력받은 값을 뒤집어 정수형으로 바꿔 정렬후 출력하면 끝이다.
'''
from sys import stdin
input = stdin.readline


lst = input().split()
n = int(lst.pop(0))
while n!=len(lst): lst += input().split()
print(*sorted(map(lambda x : int(x[::-1]), lst)), sep="\n")