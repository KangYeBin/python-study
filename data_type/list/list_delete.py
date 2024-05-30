'''
* 리스트 내부 요소 삭제

    1. remove() : 삭제할 값을 직접 지정하여 삭제한다.
    2. 내장 함수 del() : 삭제할 요소의 인덱스를 통해 삭제한다.
    3. clear() : 리스트 내부 요소 전체 삭제한다.
'''

points = [83, 99, 56, 92, 100, 78]

points.remove(92)
print(points)

del points[2]
print(points)

points.clear
print(points)