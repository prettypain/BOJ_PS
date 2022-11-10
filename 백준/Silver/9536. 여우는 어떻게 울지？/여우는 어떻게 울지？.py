'''
녹음된 텍스트 중에서 여우 소리만 추출해야 한다.
그래서 나는 여우 소리이외는 모두 제거하는 방식으로 했다.
하지만 pow를 제거하면 안되지만 강아지가 ow라고 울으면 pow가 p만 남는
불상가 발생했다. 이를 해결하기 위헤서 값 자체가 맞는지 replace 대신
단어 별로 나누어 울음소리가 일치한지 검증하는것을 통해 해결했다.
'''
n = int(input())
for _ in range(n):
    txt = input().split()
    while(t:=input())!="what does the fox say?":
        val = t.split()[2]
        for i in range(len(txt)-1, -1, -1):
            if txt[i] == val: txt.pop(i)
    print(*txt)