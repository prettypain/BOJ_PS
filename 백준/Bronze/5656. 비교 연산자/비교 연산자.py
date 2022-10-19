i = 1
while True:
    t = input()
    if "E" in t: break
    print(f'Case {i}: {"true" if eval(t) else "false"}')
    i += 1