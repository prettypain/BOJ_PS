lst = [int(input()) for i in range(4)]
if lst[0]<lst[1]<lst[2]<lst[3]:
    print("Fish Rising")
elif lst[3]<lst[2]<lst[1]<lst[0]:
    print("Fish Diving")
elif lst[0]==lst[1]==lst[2]==lst[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")
