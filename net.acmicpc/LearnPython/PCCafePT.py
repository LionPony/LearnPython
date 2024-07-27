# 피시방 알바
# https://www.acmicpc.net/problem/1453
def solution():
    N = int(input())
    seat = []
    reject = 0
    for i in input().split():
        if i in seat:
            reject += 1
        else:
            seat.append(i)
    print(reject)

solution()