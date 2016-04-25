'''
Created on 28-Nov-2013

@author: 00003179
'''



temp = {}


def caldiv(n):
    count = 0
    i = 1
    while True:
        if i > n:
            break
        elif n % i == 0:            
            count += 1
        temp[n] = count           
        i += 1
    return temp


for num in range(1,20):
    z = (num * (num+1))/2    
    caldiv(z)        

print temp.keys()
print temp.values()

