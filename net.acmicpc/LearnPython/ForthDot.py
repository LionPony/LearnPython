# 네 번째 점
# https://www.acmicpc.net/problem/3009
def solution():
    positionX = []
    positionY = []
    for i in range(3):
        x, y = map(int, input().split())
        if x in positionX:
            positionX.remove(x)
        else:
            positionX.append(x)
        if y in positionY:
            positionY.remove(y)
        else:
            positionY.append(y)
    x = positionX.pop()
    y = positionY.pop()
    print('{0} {1}'.format(x, y))

solution()