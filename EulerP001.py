'''
Created on 26-Nov-2013

@author: 00003179
'''
'''
Euler Problem #1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
sum=0
number=1000
for i in range(number):
    if i%3 == 0 or i%5 == 0 :
        sum = sum + i
print "Sum of natural numbers of multiples of 3 and 5 under", number ,"is" , sum
        