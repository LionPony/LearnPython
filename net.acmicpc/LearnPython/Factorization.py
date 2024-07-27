# 소인수분해
# https://www.acmicpc.net/problem/11653
def solution():
    n = int(input())
    if n != 1:
        i = 2
        while n > 1:
            if n%i == 0:
                print(i)
                n = n/i
            else:
                i += 1

solution()