'''
그냥 두개의 수를 각각 뒤집어서 더하고 뒤집어서 출력하면 끝~
'''
for i in range(int(input())):
    print(int(str(sum(map(lambda x : int(x[::-1]), input().split())))[::-1]))