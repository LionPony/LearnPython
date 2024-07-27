# 평균 점수
# https://www.acmicpc.net/problem/10039
def solution():
    count = 5
    scores = []
    for i in range(5):
        score = int(input())
        if score < 40 :
            scores.append(40)
        else:
            scores.append(score)
    print(int(sum(scores)/count))

solution()