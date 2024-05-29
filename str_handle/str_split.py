'''
* 문자열 분할

- split() 메서드는 구분자를 기준으로 문자열을 분할해서 리스트에 담아서 반환
'''

s1 = '떡볶이 김말이 닭강정'
print(s1.split()) # 매개값을 전달하지 않으면 공백을 구분자로 분할


s2 = '홍길동 | 대한출판사 | 2024년 5월'
data = s2.split(' | ')
print('저자 :', data[0])
print('출판사 :', data[1])
print('출판년월 :', data[2])