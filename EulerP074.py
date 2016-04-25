'''
Created on 13-Apr-2015

@author: 00003179
'''
def f(n):
        result = 1
        while n > 0:
                result *= n
                n -= 1 
        return result

total = 0
for i in range(1, 1000001):
        chain = []
        count = 0
        n = i
        while not n in chain:
                chain.append(n)
                ns = str(n)
                n = sum(f(int(d)) for d in ns)
                count += 1
        if count == 60: total += 1
print total
