# 문자열 반복
# https://www.acmicpc.net/problem/2675
def solution():
    case = int(input())
    for i in range(case):
        count, string = input().split()
        result = ''
        for j in range(len(string)):
            for k in range(int(count)):
                result += string[j]
        print(result)

solution()