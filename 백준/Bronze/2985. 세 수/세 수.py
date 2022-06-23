s = ['+','-','*','/']
List = input().split()
for i in s:
    t1 = List[1]+i+List[2]
    t2 = List[0]+i+List[1]
    if eval(t1) == int(List[0]):
        print(List[0]+"="+t1)
    elif eval(t2) == int(List[2]):
        print(t2+"="+List[2])