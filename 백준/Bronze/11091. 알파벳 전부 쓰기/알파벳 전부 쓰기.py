for _ in range(int(input())):
    cl = [0]*26
    for i in input().lower():
        if 97<= ord(i) <= 122: cl[ord(i)-97] += 1
    print("pangram" if cl.count(0)==0 else f'missing {"".join([chr(i+97) for i, v in enumerate(cl) if v==0])}')