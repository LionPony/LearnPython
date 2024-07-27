# 전자레인지
# https://www.acmicpc.net/problem/10162
def solution():
    second = int(input())
    a = 300
    b = 60
    c = 10

    a_count = second//a
    second = second%a

    b_count = second//b
    second = second%b

    c_count = second//c
    second = second%c

    if second != 0:
        print(-1)
    else:
        print('{0} {1} {2}'.format(a_count, b_count, c_count))

solution()