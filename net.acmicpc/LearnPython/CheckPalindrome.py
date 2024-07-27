# 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988
def solution():
    word = input()
    word_mid = int(len(word)/2)
    word_front = ''
    word_back = ''

    for i in range(word_mid):
        word_front += word[i]

    for i in range(len(word)-1, len(word)-word_mid-1, -1):
        word_back += word[i]

    if word_front == word_back :
        print(1)
    else:
        print(0)
        
solution()