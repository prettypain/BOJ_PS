while(s:=int(input()))!=0:
    arr = [0 for i in range(s+10)]
    for i in input().split(','): 
        if not '-' in i:
            i = int(i)
            if i > s: continue #한 페이지인데 인쇄범위를 넘는 경우
            arr[i] = 1 #한 페이지의 경우
        
        else: #범위를 가진 페이지인 경우
            l, h = map(int, i.split('-'))
            if l > h: #만약, low > high인 경우에는 이 범위는 인쇄하지 않는다.
                continue
            elif h > s:#인쇄 범위가 문서의 범위를 넘어가는 경우에는 출력할 수 있는 페이지만 출력한다.
                h = s
            for j in range(l, h+1):
                arr[j] = 1
    print(sum(arr))