while 1:
    name, age, kg = input().split()
    if name=="#":break
    print(name,"Senior" if int(age)>17 or int(kg)>79 else "Junior")