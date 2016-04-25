'''
Created on 03-Dec-2014

@author: 00003179
'''

n = input()
i = 1
while True:
    if n == 0:
        print 0
        break 
    out = i ** n
    out = str(out)
    if len(out) == n:
        print out
    if len(out) > n:
        break
    i += 1