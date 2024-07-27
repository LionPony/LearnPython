# 약수들의 합
# https://www.acmicpc.net/problem/9506
import math

def factorization(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    factors.remove(n)
    factors = list(factors)
    factors.sort()
    return factors

def printFormat(factors):
    print(factors[0], end='')
    for i in range(1, len(factors)):
        print(' + {0}'.format(factors[i]), end='')
    print()

def solution():
    end = False
    while end == False:
        num = int(input())
        if num == -1:
            end = True
        else:
            factors = factorization(num)
            if sum(factors) == num:
                print('{0} = '.format(num), end='')
                printFormat(factors)
            else:
                print('{0} is NOT perfect.'.format(num))

solution()