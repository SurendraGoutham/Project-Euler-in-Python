'''
Created on 29-Nov-2013

@author: 00003179

Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 X 53 = 49714.

What is the total of all the name scores in the file?

'''
import string

names = (open('names.txt','r')).read()
names = names.replace('"','')
names = names.split(",")
names = sorted(names)

totalScore = 0

for eachname in names: #Taking each name in all the names
    nameValue = 0
    for eachletter in eachname: #Taking each letter in eachname
        nameValue += string.ascii_uppercase.index(eachletter) + 1 #this will give the index of an alphabet, using string library                 
    totalScore += (names.index(eachname) + 1) * nameValue # Counting score position * namevalue 
print totalScore
