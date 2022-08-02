#JOI IOI
n = input()
jc = 0
ic = 0
for i in range(len(n)-2):
    if n[i:i+3] == "JOI": jc += 1
    elif n[i:i+3] == "IOI": ic += 1
print(f'{jc}\n{ic}')