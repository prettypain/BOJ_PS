'''
id는 해당 값의 레퍼런스를 알려주는 거임 즉 타겟값과 우선고가 같은 값이 있다면
그것과 레퍼런스가 같아서 id함수로는 해결이 힘들다.
그러므로 타겟의 인덱스 값을 계속해서 타겟팅 해야한다.
'''
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    c = 0
    length, idx = map(int, input().split())
    arr = list(map(int, input().split()))
    
    while True:
        #print(arr, idx)
        m = max(arr)
        if idx==0: #처리 대상이 타겟의 인덱스와 일치한 경우
            if arr[0] == m:#처리 대상이 우선도가 가장 높은 경우
                c+=1 #카운팅 추가 
                break#타겟이 몇 번째에 출력됐는지 알았기 때문에 더이상은 의미 없어서 브레이크

            #처리 대상의 우선도가 낮은 경우
            idx = len(arr)-1#뒤로 보내줘야하기떄문에 인덱스를 가장 뒤에 값으로 전환
            arr.append(arr.pop(0)) #뒤로 보내줌
             
        elif arr[0] == m: #타겟 이외의 처리 대상인 경우
            c+=1 #카운트 추가
            arr.pop(0) #처리해준다.
            idx-=1#처리 대상이 없어졌으므로 타겟의 인덱스도 땡겨준다
        else:#처리 대상이 우선도가 낮은 경우
            arr.append(arr.pop(0)) #0번째를 없애면서 그걸 뒤로 추가해준다.
            idx-=1 #이 경우에도 타겟의 인덱스를 땡겨준다.
    print(c)
