for _ in range(int(input())):
    List = [chr(i) for i in range(65,91)]
    for i in input():
        if i in List: List.remove(i)
    print(sum(map(lambda x : ord(x),List)))