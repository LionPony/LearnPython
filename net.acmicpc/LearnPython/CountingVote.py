# 개표
# https://www.acmicpc.net/problem/10102
def solution():
    v = int(input())
    votes = input()
    countA = 0
    countB = 0
    for i in list(votes):
        if i == 'A':
            countA += 1
        else:
            countB += 1
    if countA > countB:
        print('A')
    elif countB > countA:
        print('B')
    else:
        print('Tie')

solution()