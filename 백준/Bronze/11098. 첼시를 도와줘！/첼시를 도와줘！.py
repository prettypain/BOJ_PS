"""
각 값과 이름을 받아 값을 키로 이름을 벨류로 정하고
값들 중에서 가장 큰 값을 가져와 그에 매칭하는 벨류를 가져와 출력한다.
"""
import sys
input = sys.stdin.readline
for i in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        price, name = input().split()
        dic[int(price)] = name.strip()
    print(dic[max(dic.keys())])
