'''
반복되는 규칙이 있다. 1회 반복지점의 마지막까지 기억해 놓고 index over는 %로 다시 반복
시키는 형태로 카운트했다.
그리고 여러명이 같은 경우는 결과값의 최대와 같은 것은 모든 것을 출력하는 것으로 해결.
'''
input();c = [0, 0, 0]
arr = ['ABCABC', 'BABC', 'CCAABB']
for idx, val in enumerate(input()):
    for i in range(3):
        if arr[i][idx%len(arr[i])] == val: c[i] += 1
print(f'{max(c)}')
print("\n".join(["Adrian", "Bruno", "Goran"][i] for i in range(3) if (m:=max(c))==c[i]))