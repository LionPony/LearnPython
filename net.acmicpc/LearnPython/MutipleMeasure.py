# 배수와 약수
# https://www.acmicpc.net/problem/5086
def solution():
    end = False
    while end == False:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            end = True
        else:
            if b % a == 0:
                print('factor')
            elif a % b == 0:
                print('multiple')
            else:
                print('neither')

solution()