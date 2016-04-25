'''
Created on 28-Nov-2013

@author: 00003179
'''

a = []

def cal(number,count):
    
    if (number % 2 == 0):
        x = number/2
        a.append(x)
        if x <= 1:
            return count 
        else:       
            count += 1
            cal(x,count)
            return count 
    else:
        y = (3 * number) + 1 
        a.append(y)
        if y <= 1:
            return count
        else:        
            count += 1
            cal(y,count) 
            return count   
dictr={}     
maxy = 0
for i in range(1000001,10,-1):
    cal(i,0)    
    temp = maxy
    maxy = len(a) + 1
    dictr[i] = maxy
    if maxy < temp:
        maxy = temp    
    a = []


import operator

print max(dictr.iteritems(), key=operator.itemgetter(1))[0]
print max(dictr.iteritems(), key=operator.itemgetter(1))[1]
 

