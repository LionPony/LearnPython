# OX퀴즈
# https://www.acmicpc.net/problem/8958
import re

def solution():
    for i in range(int(input())):
        oxLine = input()
        oLine = re.sub('X+', ' ', oxLine)
        score = 0
        
        for i in oLine.split():
            score += int(len(i)*(len(i)+1)/2)
        print(score)

solution()