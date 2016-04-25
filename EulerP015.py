'''
Created on 28-Nov-2013

@author: 00003179
'''



from math import factorial 

n = 40      # The total number of moves for any one path (right + down)
r = 20      # The total number of right moves for any one path
 
print factorial(n) / (factorial(r) * factorial(n - r))

 

