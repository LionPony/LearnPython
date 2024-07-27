# 큰 수 A+B
# https://www.acmicpc.net/problem/10757
def solution():
    a, b = map(list, input().split())
    carry = 0
    answer = ''
    while len(a) > 0 and len(b) > 0:
        digit = carry + int(a.pop()) + int(b.pop())
        carry = digit//10
        answer = str(digit%10) + answer
    if len(a) > 0:
        for i in range(len(a)):
            digit = int(a.pop()) + carry
            carry = digit//10
            answer = str(digit%10) + answer
    else:
        for i in range(len(b)):
            digit = int(b.pop()) + carry
            carry = digit//10
            answer = str(digit%10) + answer
    if carry > 0:
        answer = str(carry) + answer
    print(answer)
    
solution()