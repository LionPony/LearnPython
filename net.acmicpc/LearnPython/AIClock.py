# 인공지능 시계
# https://www.acmicpc.net/problem/2530
def solution():
    hour, minute, second = map(int, input().split())
    timer_second = int(input())

    # Calculate separate
    timer_hour = int(timer_second/3600)
    timer_second = timer_second%3600

    timer_minute = int(timer_second/60)
    timer_second = timer_second%60

    hour += timer_hour
    minute += timer_minute
    second += timer_second

    # Round up
    if second >= 60 :
        minute += int(second/60)
        second = second%60

    if minute >= 60 :
        hour += int(minute/60)
        minute = minute%60
    
    if hour >= 24:
        hour = hour%24

    print("{0} {1} {2}".format(hour, minute, second))

solution()