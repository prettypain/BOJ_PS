import sys
input = sys.stdin.readline
while True:
    t = input().rstrip()
    if t==".":break
    stack = []
    res = True
    for i in t:
        if i in ['[', '(']:
            stack.append(i)
        elif i==']':
            if not stack:
                res = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                res = False
                break
        elif i==')':
            if not stack:
                res = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                res = False
                break
    if res and not stack:
        print('yes')
    else:
        print('no')
    #print('yes' if res and not stack else 'no')
            
