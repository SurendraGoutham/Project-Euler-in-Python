'''
Created on 26-Nov-2013

@author: 00003179
'''

# for i in range(300000000,200000000,-1):
#     if(i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 
#        and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0):
#         print i
        
i = 1
for j in range(1, 21):   
    for k in range(1, 21):
        if (i * k) % j == 0:
            i = i * k
            break
print i