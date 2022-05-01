import sys
def process(commands):
    if len(commands)==1: #단순 명령어만 주어졌을 때
        command = commands[0]
        length = len(stack)

        #조건문
        if command=="pop":
            if length<1:    print(-1)
            else:   print(stack.pop())

        elif command=="size":   print(length)
        
        elif command=="empty":  print(int(length==0))
        
        elif command=="top":
            if length==0:    print(-1)
            else:   print(stack[-1])
            
    #명령어 + 대상일 때
    else:stack.append(commands[1])
        
stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    order = sys.stdin.readline().strip()
    process(order.split())
