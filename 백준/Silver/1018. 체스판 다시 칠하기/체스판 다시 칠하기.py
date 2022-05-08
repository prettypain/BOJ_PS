"""
솔직히 백준에서 푼 문제 중에서 가장 길고 힘들게 푼것 같다..(이게 왜 실5...힘순찐이네)

이 문제의 핵심은 주어진 체스판을 8*8크기로 자른 것을 색상에 맞게 얼마나
고쳐야 하는지 그 최소 값을 구하는 문제이다.
즉 (n-7)*(m-7)의 개의 판을
-시작이 검은색일 때
-시작이 하양색일 때
의 고처야 하는 색의 갯수를 모두 모아 총 경우의 최소를 구하면 된다.
모든 체스판이 가진 색을 고친 개수 중에서 가장 작은 수를 출력.
"""
def f(arr):
    c = 0 #시작 색
    c1 = 0#시작과 반대 색
    for i in range(8):
        tmp = arr[i]
        if i==0:original = tmp[0]
        if i%2==0:
            start = original
            for k in range(8):
                if tmp[k]!=start:
                    c+=1
                else:
                    c1+=1
                start = "W" if start=="B" else "B"
        else:
            start = "W" if original=="B" else "B"
            for k in range(8):
                if tmp[k]!=start:
                    c+=1
                else:
                    c1+=1
                start = "W" if start=="B" else "B"
    return min(c,c1)
n,m = map(int, input().split())
List = [list(input()) for i in range(n)]
List2 = []
for i in range(n-7):
    tar = List[i:8+i]
    for j in range(m-7):
        temp_List = [0,0,0,0,0,0,0,0]
        for k in range(8):
            temp_List[k] = tar[k][j:8+j]
        List2.append(f(temp_List))
print(min(List2))