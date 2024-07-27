# 상근이의 친구들
# https://www.acmicpc.net/problem/5717
def solution():
    end = False
    while end == False:
        m, f = map(int, input().split())
        if m == 0 and f == 0:
            end = True
        else:
            print(m+f)

solution()