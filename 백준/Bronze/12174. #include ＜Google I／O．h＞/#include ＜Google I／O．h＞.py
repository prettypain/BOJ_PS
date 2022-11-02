'''
그냥 문자열 파싱하고 변환하고 출력하면 
'''
for case in range(int(input())):
    n = int(input())
    b = input().replace("I","1").replace("O","0")
    print(f'Case #{case+1}: ',*[chr(int(b[8*i:8+8*i],2)) for i in range(n)], sep="")
