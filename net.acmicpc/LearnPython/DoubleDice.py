# 주사위 게임
# https://www.acmicpc.net/problem/10103
def solution():
    a_score = b_score = 100

    for i in range(int(input())):
        a, b = map(int, input().split())
        if a < b:
            a_score -= b
        elif b < a:
            b_score -= a
    print(a_score)
    print(b_score)

solution()