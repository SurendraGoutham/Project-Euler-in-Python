'''
Created on 03-Dec-2014

@author: 00003179
'''

def sum_digits(k):
    s = 0
    while k:
        s += k % 10
        k /= 10
    return s

def calcPowerSum(n):
    maxSum = 0
    digitSum = 0
    for i in range(1,n+1):
        digitSum = max(sum_digits(i ** n),sum_digits(n ** i))
        maxSum = max(maxSum,digitSum)
    return maxSum

n = input()
print calcPowerSum(n)