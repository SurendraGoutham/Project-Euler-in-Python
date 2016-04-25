'''
Created on 29-Nov-2013

@author: 00003179



Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?    

'''


def CountSpiral(seq,t,n,c):
    num = n
    total = t
    count = c
    for i in range(1,5): 
        num += seq
        total += num  
        count += 1
    if(count < 2000):
        CountSpiral(seq+2,total,num,count)
    print "Spiral Number-->",seq+1,"G-total => ", total  
         
  
CountSpiral(2,1,1,0)


