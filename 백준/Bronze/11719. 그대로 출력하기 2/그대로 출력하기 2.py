#BOF를 이용한 간단한 입출력 문제이다.
#study_tip에 있는 BOF설명 부분을 보아라.

ws = ""
while True:
    try:
        ws += input()+"\n"
    except EOFError:
        break
print(ws[:len(ws)-1])
