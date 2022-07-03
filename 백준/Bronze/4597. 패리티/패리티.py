while(s:=input())!="#":
    c = s.count('1')%2==0
    print(s[:len(s)-1]+(('0' if c else '1') if s[-1] == 'e' else ('1' if c else '0')))