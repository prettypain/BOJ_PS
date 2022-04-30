dic = {
    "c=" : 0,
    "c-" : 0,
    "dz=" : 0,
    "d-" : 0,
    "lj" : 0,
    "nj" : 0,
    "s=" : 0,
    "z=" : 0
}
List = list(map(int, list(input())))
List.sort(reverse=True)
for i in List:
    print(i,end="")
