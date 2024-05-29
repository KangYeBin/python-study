'''
* 조건문 if ~ else ~

- 조건문은 조건식의 진위(참, 거짓)여부에 따라 코드를
    분기별로 다르게 실행하는 제어문이다.

- 키워드 if 뒤에 조건식을 적고, 조건식의 결과가 참이면 if문,
    거짓인 경우 else문이 실행된다.

- if문은 단독 사용이 가능하지만,
    else는 반드시 if와 함께 사용해야 한다.
'''

age = int(input('몇살이세요?: '))

if age > 19:
    print("당신은 성인입니다")
    print("주류를 구매할 수 있다")
else :
    print("당신은 성인이 아니다")
    print("주류를 구매할 수 없다")


'''
* 파이썬의 블록 구조 표현

- 타 언어는 중괄호({})로 종속 구조를 표현할 때 파이썬은 중괄호를 작성하지 않는다.

- 그 대신 콜론(:)과 들여쓰기로 블록 구조를 표현한다.

- if문 뿐만 아니라 코드의 종속 구조를 나타내는
    모든 문법에서 (반복문, 함수 선언...) 콜론과 들여쓰기를 사용한다.
    파이썬의 권장 들여쓰기 횟수는 스페이스바 4회.
    들여쓰기는 모든 횟수가 통일되어야 한다.
    콜론(:) 이후에는 반드시 줄 개행이 진행되어야 한다.
'''