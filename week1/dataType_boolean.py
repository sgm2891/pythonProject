#논리 자료형

"""
boolean, bool 또는 논리 자료형이라 부르는 이 자료형은 True False 총 2개의 값만 존재한다.

조건문에서 참과 거짓을 구분하는데 쓰인다.
"""

a = True 

b = False #직접 True 와 False를 넣음으로써 논리 자료형을 선언할 수 있다.


#논리 연산자
"""
논리 자료형끼리 연산할 수 있는 논리 연산자는 and, or 그리고 not 이 있다.

and: 둘다 참일 때 True, 그 이외의 경우는 모두 False 이다.

or: 둘 중 하나 이상이 참이면 True, 둘다 거짓일 경우만 False이다.

not: 논리 자료형 앞에 쓰이며 True를 False로, False를 True로 바꿔 준다.
"""

c = a and a #True and True 이기 때문에 True

d = a and b #True and False 이기 때문에 False

e = a or b #True or False 이기 때문에 True

f = b or b # False or False 이기 때문에 False

g = not a #not True 이기 때문에 False

h = not b #not False 이기 때문에 True


#비교 연산자
"""
두 값을 비교하기 위해 비교 연산자를 사용할 수 있다.

비교 연산자에는 ==, !=, <, >, <=, >= 가 있다. 이를 아래의 예제를 통해 살펴보자
"""

i = 2*5 == 10 
#2*5와 10이 같은 값은가? 에 대한 해답을 리턴한다. 
#컴퓨팅 언어에선 등호(=)는 대입이고 ==는 비교임을 주의하자

j = 5 != 5 #!= 는 not equal 과 같은 뜻이다. 두 값이 다를 경우 참을 리턴한다.

j = 2 > 5 #대소를 비교하고 이에 대한 결과를 리턴한다. <의 경우도 마찬가지

k = 3 <= 4 #3이 4보다 작거나 같을 때 True를 리턴한다. >= 경우도 마찬가지


#bool() 함수
"""
아직 함수에 대해 배우지 않았지만 bool 자료형의 특성을 알기 위해 잠깐 이용하겠다.

bool(a) 는 a가 True 인지 False 인지 판단하는 함수이다.

이 때 a는 어떤 자료형이어도 상관 없다. (문자열, 숫자여도 상관이 없다.)

bool 자료형일 때는 그대로 출력이 된다.

문자열의 경우 빈 문자열이면 False, 그 이외는 True를 리턴한다.

리스트의 경우 빈 리스트이면 False, 그 이외는 True를 리턴한다.

숫자의 경우 0이면 False, 그 이외는 True를 리턴한다.
"""

l = bool(True) #bool() 내부의 값이 bool 자료형이면 bool 자료형 그대로를 리턴한다.

m = bool("") #빈 문자열의 경우 False를 리턴한다.

n = bool("not empty") #빈 문자열이 아닌 경우 True를 리턴한다.

o = bool([]) #빈 리트스틑 False를 리턴한다.

p = bool([[1,2],"string"]) #빈 리스트가 아닌 경우 True를 리턴한다.

q = bool(0) #0인 경우  False를 리턴한다.

r = bool(-3.14) #0이 아닌 경우 True를 리턴한다.