'''
Created on 26-Nov-2013

@author: 00003179
'''

for i in range(900,999):
    for j in range(900,999):
        k = i * j        
        k = str(k)
        if k == k[::-1]:
            print " ya itz me ", k