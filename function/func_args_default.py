'''
# 인수의 기본값

- 파이썬에서는 인수의 기본값을 설정하여
    자주 바뀌지 않는 매개값은 기본값으로 처리하게 한다.
'''

def calc_stepsum(begin, end, step = 1):
    sum = 0
    for n in range(begin, end + 1, step):
        sum += n
    return sum

print(calc_stepsum(1, 10))
print(calc_stepsum(1, 10, 2))


# 기본값이 없는 것을 왼쪽으로 몰아서 작성해야 한다
def calc_sum(end, begin = 0, step = 1):
    sum = 0
    for n in range(begin, end + 1, step):
        sum += n
    return sum

print(calc_sum(100))