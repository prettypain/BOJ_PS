while True:
    void = 1
    n = input()
    if n=='0':break
    for i in n:
        i = int(i)
        if i==1:
            void +=2
        elif i==0:
            void +=4
        else:
            void += 3
        void+=1
    print(void)
