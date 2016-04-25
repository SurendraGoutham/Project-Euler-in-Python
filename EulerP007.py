'''
Created on 27-Nov-2013

@author: 00003179
'''
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# count = 1
# num = 2
# limit = 10
# while True:
#     if count > limit:
#         break
#     elif is_prime(num):
#         print count, " is ", num
#         count += 1
#     num += 1

x = 0
for i in range(2,2000001):
    if is_prime(i):
        x += i

print x 