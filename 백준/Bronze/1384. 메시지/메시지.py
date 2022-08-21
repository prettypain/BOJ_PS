'''
이거 브론즈 문제 맞나용....
실버5 문제도 평균 2회정도면 푸는데 이건 4번이나 틀리고 풀었네요 힝...
(물론 제 머리가 이상해서 출력형식이랑 간단한거 까먹어서 두번 틀리긴했습니다 ㅎ)


이 문제는 생각보다 간단합니다.
예를들어
5
Ann P N P P
Bob P P P P
Clive P P P P
Debby P N P P
Eunice P P P P
0
라면
Ann입장에서 보기전에
Ann의 왼쪽친구 즉 Ann이 이름을 적고 왼쪽으로 넘겼을때 그것을 받은 사람은 "Eunice"입니다.
(이걸 보면 원형 자료구조 또는 리스트의 음수 개념이 생각난다면 칭찬해드림)
다시 Ann입장에서 보면 P N P P로 왼쪽으로 + 2 방향에 친구에게 욕을 먹었네요
Ann -> Eunice -> Debby
아 우리 Debby친구 Ann에게 욕설을 했어요.
이 친구를 출력하고
다음친구는 욕이 없네요. 넘어갑시다 * 2

이번 친구는 Debby군요
Debby는 P N P P로 욕설을 한번 먹었고 Ann과 똑같은 패턴이군요
그럼 왼쪽으로 두번 가보면?
Debby -> Clive -> Bob
Bob친구가 욕설을 했군요!

여기서 규칙성을 보자면
나한테 욕한 그놈 = (내 위치) - (N의 인덱스)
로 나옵니다.(이미 위치를 구해 찾은 N은 P로 교화시켰다고 가정할 때)
이 다음부턴 쉽습니다.(저처럼 print()추가 까먹고 한번 더 틀리지 마시고 추가하세용 ㅠ)
'''
from sys import stdin
input = stdin.readline #대충 빨리 입력받는 방법인데 문자열 다룰때는 rstrip()붙이세요
group = 0
while(n:=int(input()))!=0:
    lst = [input().rstrip().split() for i in range(n)]
    name = [i[0] for i in lst]
    print(f'Group {group+1}')
    pc = 0 #print count 
    for i in lst:
        letter = i[1:]
        c = letter.count("N")
        for j in range(c):
            who = name[name.index(i[0]) - letter.index("N") - 1]
            print(f'{who} was nasty about {i[0]}')
            letter[letter.index("N")] = ""
        pc += c
    if pc==0:
        print("Nobody was nasty")
    group += 1
    print()