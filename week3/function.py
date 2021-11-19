'''
함수란 입력을 받고 원하는 값을 출력하는 것을 말한다.

우리가 흔히 알고 있는 함수 f(x, y)와 동일하다 생각하면 된다.

간단한 일차함수 3x + 5 부터 아주 복잡한 함수 또한 파이썬에서 만들 수 있다.

그렇다면 이런 함수가 필요한 이유는 무엇일까?

만약에 우리가 어떤 함수를 한번만 사용한다면 그냥 in line 으로 적는것이 효율적이다.

그러나 만약에 같은 함수를 여러번 사용해야하고 변수들을 각각 다르게 해야한다면 어떨까?

매번 복사 붙여 넣기를 해야하고 변수를 수정해야한다.

이러한 번거로움을 피하기 위해 우리는 함수를 이용한다.

함수의 선언은 다음과 같이 한다.

def name(a,b,c):
    실행문...
    return 리턴값

이제는 직감적으로 알 수 있듯 함수 내외의 구분 역시 들여쓰기로 구분한다.

return 뒤에 값은 함수가 가지는 자체 값이다.

위의 경우에

result = name(a,b,c) 를 하게 되면 result 변수에 리턴값이 저장된다.

예시를 통해 한번 확인해보자
'''

def return_one():
    return 1

def return_nothing():
    print("nothing return")

def add(a, b):
    return a + b


# ax^2 + bx + c
def quadraticFormula(a,b,c): 
    
    answer1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    answer2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

    return [answer1, answer2]

'''
만약에 내가 받을 값이 정확하게 몇개인지 모르면 어떻게 될까?

일반적인 방법으로 두가지가 있다.

input 변수 앞에 *만 붙이면 된다.

def name(*args):
    실행문...

args는 그냥 임의의 문자이고 다른 문자를 사용해도 된다.

또는 input으로 list를 받으면 된다.

def name(list_input):
    실행문...

다음의 예시로 한번 자세히 알아보자
'''

def sum_arg(*args):
    
    sum = 0
    for i in args:
        sum += i
    return sum


def sum_list(list_):
    sum = 0
    for i in list_:
        sum += i
    return sum


'''
일부 변수는 일반적으로 사용되는 값이 존재할 수 있다.

예를 들어서 연세대학교 내부에서 방문자 정보를 입력받고 출력하는 함수가 있다고 생각해보자.

일부 교환학생 또는 외부인사가 있을 수 있지만 대부분은 연세대학교 학생일 것이다.

그렇다면 매번 연세대학교 학생임을 기입하는 것 보단 기본값을 연세대학교 학생이라고 설정하면 
번거로움을 줄일 수 있을 것이다.

아래의 예시를 보고 어떻게 사용하는지 알아보자.
'''

def personData(name, age, identity = '연세대학교 학생'):
    print('이름: ' + name)
    print('나이: ' + str(age))
    print('소속: ' + identity)

'''
만약 연세대학교 학생이라면 다음과 같이 함수 호출을 하면된다.

personData('송규민', 22)

그렇지 않다면 다음과 같이 호출하면 된다.

personData('Elon Musk', 49, "Tesla's techno king")

여기서 주의할 점은 기본값을 설정하는 변수는 맨 뒤로 빼야한다는 것이다. (개수는 상관없다)

예를 들어서

def sampleFunc(a,b,c=1,d=2):
    실행문...

은 가능하나

def sampleFunc(a,b=1,c,d=2):
    실행문...

또는 
def sampleFunc(a = 1, b):
    실행문...


과 같은 형태는 불가능하다.
'''


'''
마지막으로 다음함수가 어떤 함수인지 한번 다같이 생각해보는 시간을 가져보면서 마무리 하도록 하자.
'''

def whatsThis(n): #n 은 자연수
    if n == 1 or n==2:
        return 1
    else:
        return whatsThis(n-1) + whatsThis(n-2)

for i in range(1,11):
    a = whatsThis(i)
    print(whatsThis(i))