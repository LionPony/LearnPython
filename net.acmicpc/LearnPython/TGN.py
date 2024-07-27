# TGN
# https://www.acmicpc.net/problem/5063
def getdiff(a, b):
    if a > b:
        return a-b
    elif b > a:
        return b-a
    else:
        return 0

def solution():
    for i in range(int(input())):
        r, e, c = map(int, input().split())
        if r > e :
            print('do not advertise')
        else:
            adEffect = getdiff(r,e)
            if adEffect > c:
                print('advertise')
            elif adEffect < c:
                print('do not advertise')
            else:
                print('does not matter')

solution()