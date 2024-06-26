
'''
* 문자열 포맷팅

- 포맷팅은 문자열 사이에 다른 타입의 데이터를 넣어서 문자열을 조립하는 방식
'''

apple = 3
print('사과가 ', apple, '개 있습니다.', sep='')     # sep 옵션으로 공백 생략
print('사과가 %d개 있습니다.' %apple)


'''
- 여러 개의 데이터도 하나의 문자열에 포맷팅할 수 있는데
    이때는 % 연산자 뒤에 나열한 변수를 ()로 묶어준다
'''

month = 12
day = 25
anni = '크리스마스'
print('%d월 %d일은 %s입니다' %(month, day, anni))


'''
* format 함수를 사용한 형식 지정 출력

- 문자열에 format 함수를 사용하면 서식 문자를 지정하는 것보다
    더 유용하고 편하게 문자열 포맷팅을 할 수 있다
'''

print('{}월 {}일은 {}입니다'.format(month, day, anni))


# 소수점 표현
pi = 3.141592
print('원주율은 {:0.3f}입니다'.format(pi))


# f 문자열 포맷팅
# 파이썬 3.6 버전 이후로 사용 가능
# 접두어 f를 문자열 앞에 붙여서 사용
print(f'{month}월 {day}일은 {anni}입니다')


# {} 안에서는 수식도 사용 가능
salary = 300
print(f'보너스를 합한 월급 : {salary + 100}')
print(f'원주율은 {pi:0.2f} 입니다')