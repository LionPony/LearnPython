# 크냐?
# https://www.acmicpc.net/problem/4101
def solution():
    end = False
    while end == False :
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            end = True
        else :
            if a > b :
                print('Yes')
            else:
                print('No')

solution()