List = sorted(list(map(int, input().split())))
dic = {"A" : List[0],
       "B" : List[1],
       "C" : List[2]
}
for i in input():
    print(dic[i],end=" ")
