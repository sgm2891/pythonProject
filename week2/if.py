"""
if 문은 특정 조건을 만족할 때만 문장을 실행시키게 해주는 '조건문' 이다.

if 문의 구조는 다음과 같다

if a:
    실행문1
elif b:
    실행문2
else:
    실행문3


if 뒤의 a 는 bool(a) 의 값을 리턴하여 참 또는 거짓을 판별한다. 즉 a 자리에는 bool 자료형 뿐만 아니라 어떤 자료형이 들어가도 상관없다.

만약 bool(a) 가 True 라면 실행문1을 실행하고 if문을 빠져나온다.(else 뒤로 빠져나온다.)

이 때 실행문에는 들여쓰기를 사용해야한다. 들여쓰기는 스페이스 4번 "    " 또는 tab키로 구분한다. " " 

파이썬에서는 둘다 들여쓰기로 인식을 하지만 한 스크립트 내에서는 둘 중 하나를 선택하여 통일하여 사용하여야 한다.

파이썬 표준으로는 스페이스 4번을 쓰는 것을 권장하고 있다.

VSC에서는 .py 파일에서는 자동으로 탭을 하면 공백으로 치환하여 주기 때문에 걱정하지말자.

단 외부에서 코드를 복사해 올 때에는 탭으로 되어있는 코드가 있을 수 있으니 주의하도록 하자.


elif 는 else if 라는 의미이다. if 에서 a 가 거짓일 경우 elif 문을 실행한다. elif는 하나의 if문에서 여러개가 사용될 수 있다.

elif도 마찬가지로 이후에 나오는 조건이 참이라면 실행문을 실행하고 if 문을 빠져나온다.


else 는 if 그리고  elif가 모두 실행되지 않았을 때 else 의 실행문이 실행된다. else문은 if 문에서 꼭 써야할 필요는 없다.

예외 처리가 필요할 때 사용된다.

"""

#pass 임을 판별 해 주는 if문
score1 = float(input("점수를 입력하세요: "))
if score1 >= 50:
    print("pass 입니다.")

#pass 임을 판별 해 주고 non pass 또한 출력해주는 if 문
score2 = float(input("점수를 입력하세요: "))
if score2 >=50:
    print("pass 입니다.")
else:
    print("non-pass 입니다.")

#나이의 초, 중, 말 을 구분해주는 if 문
age = int(input("나이를 입력하세요: "))
age = age
onesPlace = age % 10

if onesPlace < 3:
    print("초")
elif onesPlace <7:
    print("중")
else:
    print("말")


