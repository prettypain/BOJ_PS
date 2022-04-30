List = list(map(int, list(input())))#문자열에 list를 주면 1나씩 쪼개진다. 그 쪼개진걸 정수로 바꾼다.
List.sort(reverse=True) #reverse 라는 옵션을 True로 설정함으로써 내림차순이 된다.
for i in List:#정렬된 값들을 i에 넣어 반복한다.
    print(i,end="")
