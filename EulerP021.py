'''
Created on 29-Nov-2013

@author: 00003179

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''
'''
def calcDivisors(k):    
    for i in range(1,k):
        if(k % i == 0):                      
            print i
'''

def SumofDivisors(k):
    sumy = 0
    for i in range(1,k):
        if(k % i == 0):
            sumy += i   
    return sumy


sumy2 = 0
for i in range(1,1000001):  
    k1 = SumofDivisors(i)
    k2 = SumofDivisors(k1)    
    if((k2==i) and (k1!=i)) :
        #print i, " is an amicable number "       
        sumy2 += i 
        
print "Total sum is ",sumy2




    