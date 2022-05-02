import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b = input().split()
    c=0
    for i in range(int(a),int(b)+1):
        c+=str(i).count('0')
    print(c)
