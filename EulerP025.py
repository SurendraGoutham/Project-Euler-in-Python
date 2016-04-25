'''
Created on 29-Nov-2013

@author: 00003179
'''
def calFib():
    
    i = x = 0
    y = z = 1
        
    while True:        
        if len(str(z)) == 1000:
            print i+1 , 'is' , z
            break
        z = x + y    
        x = y
        y = z 
        i += 1   

calFib()