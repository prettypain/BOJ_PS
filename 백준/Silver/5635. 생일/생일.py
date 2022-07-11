y = {}
for i in range(int(input())):
    day, mon, year = map(int,(t:=input().split())[1:])
    name = t[0]
    if y.get(year): #year이 있다면
        if y[year].get(mon): #mon이 있다면
            y[year][mon][day] = name
        else: #mon이 없다면
            y[year][mon] = {day : name}
    else: #year이 없다면
        y[year] = {
            mon:{
                day : name
                 }
            }
#가장 젊은 사람과, 가장 늙은 사람을 찾기
print(y[max(y.keys())][max(y[max(y.keys())])][max(y[max(y.keys())][max(y[max(y.keys())])])])
print(y[min(y.keys())][min(y[min(y.keys())])][min(y[min(y.keys())][min(y[min(y.keys())])])])