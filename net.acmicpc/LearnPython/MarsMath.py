# 화성 수학
# https://www.acmicpc.net/problem/5355
def solution():
    count = int(input())
    for i in range(count):
        operation = input().split()
        start = float(operation[0])
        for j in operation[1:]:
            if j == '@' :
                start *= 3
            elif j == '%' :
                start += 5
            elif j == '#' :
                start -= 7
        print("{0:.2f}".format(start))

solution()