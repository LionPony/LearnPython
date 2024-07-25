# 오븐 시계
# https://www.acmicpc.net/problem/2525
def solution():
    hour, minute = map(int, input().split())
    timer = int(input())

    if minute + timer >= 60 :
        hour = (hour+int((minute+timer)/60))%24
        minute = (minute+timer)%60
    else:
        minute += timer

    print("{0} {1}".format(hour, minute))

solution()