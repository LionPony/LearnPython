# A+B-7
# https://www.acmicpc.net/problem/11021
def solution():
    count = int(input())
    for i in range(count):
        a, b = map(int, input().split())
        print("Case #{0}: {1}".format(i+1, a+b))

solution()