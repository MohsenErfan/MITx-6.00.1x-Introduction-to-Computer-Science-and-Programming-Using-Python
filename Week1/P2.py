"""Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2"""

s = 'azcbobobegghaklbob'
size = len(s)
a = 0
for count in range(size-2):
    if s[count] == 'b'and s[count+1]=='o' and s[count+2]=='b':
        a+=1
print('Number of times bob occurs is: ', a)
