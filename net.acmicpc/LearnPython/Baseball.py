# Baseball
# https://www.acmicpc.net/problem/10214
def solution():
    for i in range(int(input())):
        korea = yonsei = 0
        for j in range(9):
            y, k = map(int, input().split())
            korea += k
            yonsei += y
        if korea > yonsei:
            print('Korea')
        elif yonsei > korea:
            print('Yonsei')
        else:
            print('Draw')

solution()