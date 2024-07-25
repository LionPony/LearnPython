# 나머지
# https://www.acmicpc.net/problem/10430
def solution():
    a, b, c = map(int, input().split())
    print(int(a+b)%c)
    print(int((a%c)+(b%c))%c)
    print(int((a*b)%c))
    print(int((a%c) * (b%c))%c)

solution()