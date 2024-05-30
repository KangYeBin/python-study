'''
* 사전 (Dictionary)

- 사전은 키(key)와 값(value)의 쌍을 저장하는 대용량의 자료구조.

- 사전은 타 언어에서는 Map이라고도 부르며 연관 배열이라고도 한다.

- 사전을 정의하는 기호는 {}이고,
    괄호 안에 데이터를 key : value 형태로 나열하여 저장한다.
'''

student = {'멍멍이':'홍길동', '야옹이':'박영희', '짹짹이':'김철수'}
print(type(student))
print(len(student))


'''
- 사전에 사용되는 key값은 중복값을 가질 수 없고, 변경도 안 된다.

- 반면에 value값은 중복을 허용하고, 데이터를 자유롭게 편집 가능하다.

- 사전 내부에 저장된 데이터를 검색할 때는
    인덱스 대신 key를 사용합니다. (시퀀스 자료형이 아님)
'''
print(student['멍멍이'])
print(student['짹짹이'])
# print(student['메뚜기'])
# 자바에서는 없는 key를 주면 null을 주지만 python에서는 에러


# in 키워드를 사용하여 key의 존재 유무를 파악할 수 있다
# True / False로 리턴
print('멍멍이' in student)
print('메뚜기' in student)
