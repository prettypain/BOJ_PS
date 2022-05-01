import sys
def process(commands):
    if len(commands)==1: #단순 명령어만 주어졌을 때
        command = commands[0]
        length = len(que)

        #조건문
        if command=="pop":
            if length<1:    print(-1)
            else:   print(que.pop(0))
        elif command=="size":   print(length)
        elif command=="empty":  print(int(length==0))
        elif command=="front":
            if length==0:    print(-1)
            else:   print(que[0])
        elif command=="back":
            if length==0:    print(-1)
            else:   print(que[-1])
    #명령어 + 대상일 때
    else:que.append(commands[1])
        
que = []
n = int(sys.stdin.readline())
for _ in range(n):
    order = sys.stdin.readline().strip()
    process(order.split())
