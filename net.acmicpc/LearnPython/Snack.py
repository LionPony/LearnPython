# 과자
# https://www.acmicpc.net/problem/10156
def solution():
    k, n, m = map(int, input().split())
    need = k*n
    if m < need:
        print(need-m)
    else:
        print(0)

solution()