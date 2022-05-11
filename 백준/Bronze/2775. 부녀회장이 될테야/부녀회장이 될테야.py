
'''
a층에 i호는 a가 1이상 and i가2이상일 때
a층에 i호에 사는 사람 수 = a층에 (i-1)호에 사는 사람 수 + (a-1)층 i호에 사는 사람 수
가 성립한다.

'''
List = [list(range(1,15))]
for i in range(14):
    tmp = [1]
    for j in range(1,14):
        tmp.append(tmp[j-1] + List[i][j])
    List.append(tmp)
n = int(input())
for i in range(n):
    arr = [int(input()),int(input())]#k, n
    people = List[arr[0]][arr[1]-1]#해당 층에 사는 사람 수 : 즉 결과값
    print(people)