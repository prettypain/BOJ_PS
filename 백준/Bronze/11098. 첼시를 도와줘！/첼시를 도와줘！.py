import sys
dic = {}
input = sys.stdin.readline
n = int(input())
for i in range(n):
    dic = {}
    for _ in range(int(input())):
        price, name = input().split()
        dic[int(price)] = name.strip()
    print(dic[max(dic.keys())])
