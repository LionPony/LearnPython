# 최소공배수
# https://www.acmicpc.net/problem/1934
def solution():
    count = int(input())
    for i in range(count):
        a, b = map(int, input().split())
        print(int(a*b/euclidean(a, b)))

def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, a%b)

solution()