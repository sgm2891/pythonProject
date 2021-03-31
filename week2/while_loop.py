"""
while문도 for 문과 같은 반복문이다.

for 문은 in 뒤에 있는 리스트의 개수만큼 반복했다면

while 문은 특정 조건을 만족하지 않을 때 까지 반복한다.

while 문의 구조는 다음과 같다.

while 조건문:
    실행문

while문에서 조건문이 False 일 경우 실행문을 실행하지 않고 종료한다.
"""

count = 0
result = 0
while (count < 10):
    result = result + count
    print(result)
    count = count + 1

input() #일시정지

"""
while 문을 특정 조건에서 강제로 빠져나오고 싶다면 break문을 사용하면 된다.
"""
count = 0
while(True):
    print(count)
    count = count + 1
    if count > 10 :
        break

input() #일시정지
"""
어떨 때 while 문을 쓸까?

for문 대신 while문을 쓰는 경우는 보통 이 반복문이 언제 끝날지 정확하게 알지 못할 때 이다.

다음 코드는 가위바위보를 하여 이길 때 까지 반복하는 코드이다.
"""
import random #python 내장 모듈 중 난수를 이용할 수 있는 모듈

while True:
    you = int(input("선택하세요 (가위:0 바위:1 보:2): "))
    com = random.randrange(0,3) #0~2까지의 자연수 선택

    if com == 0:
        print("컴퓨터는 가위를 냈습니다.")
    elif com == 1:
        print("컴퓨터는 바위를 냈습니다.")
    else:
        print("컴퓨터는 보를 냈습니다.")
    
    if (you-com)%3 == 0:
        print("비겼습니다.")
    elif (you-com)%3 == 1:
        print("당신이 이겼습니다. 게임을 종료합니다.")
        break
    else:
        print("당신이 졌습니다.")
    