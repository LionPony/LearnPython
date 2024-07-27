# 수들의 합
# https://www.acmicpc.net/problem/1789
def solution():
    s = int(input())
    i = 2
    while i < s:
        s -= i
        i += 1
    print(i-1)

solution()