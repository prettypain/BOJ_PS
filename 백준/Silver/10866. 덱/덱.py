import sys
input = sys.stdin.readline
n = int(input())
deq = []#대충 리스트를 덱처럼 사용할 예정

for i in range(n):
    tmp = input().split()
    order = tmp[0]
    if len(tmp)==2: #명령어와 데이터인 경우
        tar = tmp[1]
        if order=="push_front":
            deq.insert(0,tar)
        else:
            deq.append(tar)
    else: #단순 명령어인 경우
        LD = len(deq)
        if LD==0 and order in ["pop_front", "pop_back", "front", "back"]: print(-1)
        else:
            if order=="pop_front": print(deq.pop(0))
            elif order=="pop_back": print(deq.pop(-1))
            elif order=="size": print(LD)
            elif order=="empty": print(1 if LD==0 else 0)
            elif order=="front": print(deq[0])
            else: print(deq[-1])