'''
Created on 29-Nov-2013

@author: 00003179
'''



def facty(n):
    if n == 1:
        return 1
    else:
        return n * facty(n-1)   


s = facty(6)
print sum(map(int, str(s)))