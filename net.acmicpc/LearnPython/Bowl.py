# 그릇
# https://www.acmicpc.net/problem/7567
def solution():
    bowls = list(input())
    bowl = bowls.pop()
    height = 10
    while(len(bowls) > 0):
        if bowl == bowls[-1]:
            height += 5
        else:
            height += 10
        bowl = bowls.pop()
    print(height)

solution()