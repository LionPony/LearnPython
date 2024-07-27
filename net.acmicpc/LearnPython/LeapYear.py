# 윤년
# https://www.acmicpc.net/problem/2753
def solution():
    year = int(input())
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(1)
            else:
                print(0)
        else:
            print(1)
    else:
        print(0)

solution()