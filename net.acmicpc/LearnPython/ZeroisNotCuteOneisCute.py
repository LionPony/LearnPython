# 0 = not cute / 1 = cute
# https://www.acmicpc.net/problem/10886
def solution():
    countZero = 0
    countOne = 1
    for i in range(int(input())):
        if int(input()) == 1:
            countOne += 1
        else:
            countZero += 1
    if countOne > countZero:
        print('Junhee is cute!')
    else:
        print('Junhee is not cute!')
    return 0

solution()