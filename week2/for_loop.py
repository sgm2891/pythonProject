"""
for 문은 반복적으로 하나의 동작을 반복해야할 때 사용된다.

for문의 구조는 다음과 같다.

for 변수 in 리스트:
    실행문

앞서 본 if 문과 마찬가지로 for 내부와 외부는 들여쓰기로 구분한다.

for 문은 in뒤에 있는 리스트에 있는 값을 변수에 할당하고 리스트가 끝날 때 까지 이를 반복한다.
"""

for i in [1,3,5,7,9]:
    print(str(i) + "의 제곱: " + str(i**2))


input() # 일시정지
"""
for 문과 같이 사용하면 좋은 range함수

정확하게 말하자면 for 문의 in 뒤에는 리스트 이외에도 모든 iterable한 객체, 

객체의 원소를 차례로 꺼내어 반복적인 작업을 할 수 있는 객체가 들어갈 수 있다.

range 또한 iterable한 객체이다.

range의 선언은 다음과 같다.

range(a, b, c) a부터 b 미만의 숫자를 c의 간격으로 포함하는 객체

예)  range(1, 11, 3) => [1,4,7,10]

range(a, b) = range(a, b, 1)

range(a) = range(0, a)
"""

for i in range(10):
    print(i)

input() #일시정지

for i in range(5,11):
    print(i)

input() #일시정지

for i in range(1,10,2):
    print(str(i) + "의 제곱: " + str(i**2))

input() #일시정지

"""
잘 쓸일은 없겠지만 string 또한 iterable 한 객체이다.
"""

s = "string"

for i in s:
    print(i)