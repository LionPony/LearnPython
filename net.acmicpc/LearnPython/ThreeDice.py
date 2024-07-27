# 주사위 세 개
# https://www.acmicpc.net/problem/2480
def solution():
    dice = {}
    for i in input().split():
        if i in dice:
            dice[i] = dice[i]+1
        else:
            dice[i] = 1
    
    same = len(dice.keys())
    if same == 1:
        for key in dice.keys():
            print(10000+int(key)*1000)
    elif same == 2:
        for key in dice.keys():
            if dice[key] == 2:
                print(1000+int(key)*100)
    else:
        print(int(max(dice.keys()))*100)

solution()