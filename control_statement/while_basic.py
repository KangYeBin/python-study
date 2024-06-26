'''
* 반복문 (loop)

- 반복문은 유사한 명령을 횟수를 지정하여 반복 실행하는 제어문이다.

- 파이썬의 반복문 키워드는 while, for ~ in 이 있다.
'''

# while문에 필요한 3요소 : 제어변수(begin), 조건식(end), 증감식(step)

i = 1   # begin
total = 0

while i <= 10:  #end
    total += i
    i += 1

print('1부터 10까지의 누적합 :', total)


'''
- 정수 2개(x, y) 입력받아 x부터 y까지의 누적합을 while을 사용하여 구하는 코드를 작성하라.
 ex) "x부터 y까지의 누적합계: z"

- 처음에는 x가 무조건 작은 값이 들어올 것이다 라고 가정하고 작성한다.

- 그 후, 만약 x가 y보다 더 큰 값이 들어왔을 때는, 어떻게 대처할 지 생각해보기. (while을 2번쓰는 건 아니에요~)
'''

x = int(input('x : '))
y = int(input('y : '))

if x > y:
    x, y = y, x

i = x
total = 0
while i <= y:
    total += i
    i += 1

print(x,'부터', y,'까지의 누적합계 :', total)
