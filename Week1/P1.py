"""Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""

s = 'azcbobobegghakl'
s = s.lower()
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for letter in s:
    if letter in vowels:
        count += 1
print ('Number of vowels: ', count)


#2nd version without list
s = s.lower()
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or\
     letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print ('Number of vowels: ', count)
