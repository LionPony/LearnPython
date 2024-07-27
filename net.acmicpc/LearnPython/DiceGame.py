# 주사위 게임
# https://www.acmicpc.net/problem/2476
def game(input):
    dice = {}
    for i in input.split():
        if i in dice:
            dice[i] = dice[i]+1
        else:
            dice[i] = 1
    
    same = len(dice.keys())
    if same == 1:
        for key in dice.keys():
            money = 10000+int(key)*1000
    elif same == 2:
        for key in dice.keys():
            if dice[key] == 2:
                money = 1000+int(key)*100
    else:
        money = int(max(dice.keys()))*100
    return money

def solution():
    moneys = []
    for i in range(int(input())):
        moneys.append(game(input()))
    print(max(moneys))

solution()