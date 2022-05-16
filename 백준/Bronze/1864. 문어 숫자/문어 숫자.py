dic = {
    "-" : 0,
    "\\" : 1,
    "(" : 2,
    "@" : 3,
    "?" : 4,
    ">" : 5,
    "&" : 6,
    "%" : 7,
    "/" : -1
}
while True:
    user = input()
    if user=="#":break
    s,j = 0,0
    for i in range(len(user)-1,-1,-1):
        s+= dic[user[j]] * (8**i)
        j+=1
    print(s)