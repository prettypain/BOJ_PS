'''
가중치부분이 조금 어려울뿐 나머지는 쉬움
가중치는 뒤에서부터 앞으로 증가하므로
반복문을 짤때 살짝 머리를 써야함
'''
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    en, num = input().split("-")
    num = int(num)
    t = sum([((ord(en[i])-65)*(26**(len(en)-1-i))) for i in range(len(en))])
    print("nice" if abs(t-num)<= 100 else "not nice")