from sys import stdin
for i in range(int(stdin.readline())):
    t = ""
    while(s:=stdin.readline())!="\n":
        t+=s.rstrip()
    res =f'{(1-t.count("#")/len(t))*100:.1f}'
    if res[-1] == '0':res = int(float(res))
    print(f'Efficiency ratio is {res}%.')