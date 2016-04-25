'''
Created on 28-Nov-2013

@author: 00003179
'''


table = [[int(n) for n in s.split()] for s in open('triangle.txt').readlines()]
 
for row in range(len(table)-1, 0, -1):
    for col in range(0, row):
        table[row-1][col] += max(table[row][col], table[row][col+1])
 
print "Max Sum is = ", table[0][0]
 

