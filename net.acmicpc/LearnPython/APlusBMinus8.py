# A+B-8
# https://www.acmicpc.net/problem/11022
def solution():
    count = int(input())
    for i in range(count):
        a, b = map(int, input().split())
        print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))

solution()