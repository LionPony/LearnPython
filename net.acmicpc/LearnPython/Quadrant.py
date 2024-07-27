# 사분면
# https://www.acmicpc.net/problem/9610
def solution():
    Q1 = Q2 = Q3 = Q4 = AXIS = 0
    for i in range(int(input())):
        x, y = map(int, input().split())
        if x == 0 or y == 0:
            AXIS += 1
        else:
            if x > 0:
                if y > 0:
                    Q1 += 1
                else :
                    Q4 += 1
            else:
                if y > 0:
                    Q2 += 1
                else :
                    Q3 += 1
    print("Q1:", Q1)
    print("Q2:", Q2)
    print("Q3:", Q3)
    print("Q4:", Q4)
    print("AXIS:", AXIS)

solution()