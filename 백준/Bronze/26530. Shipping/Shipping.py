for _ in range(int(input())):print(f'${sum([float((t:=input().split())[2])*int(t[1]) for i in range(int(input()))]):.2f}')