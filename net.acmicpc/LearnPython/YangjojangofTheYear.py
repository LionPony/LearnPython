# Yangjojang of The Year
# https://www.acmicpc.net/problem/11557
def solution():
    for i in range(int(input())):
        accountBook = {}
        for j in range(int(input())):
            name, alcohol = input().split()
            accountBook[int(alcohol)] = name
        print(accountBook[max(accountBook.keys())])

solution()