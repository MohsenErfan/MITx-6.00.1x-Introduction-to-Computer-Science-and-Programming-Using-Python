"""Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in
which the letters occur in alphabetical order. For example,

if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is beggh
In the case of ties, print the first substring. For example,
 if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is abc"""
s = 'azcbobobegghakl'

current =s[0]
max_len = 0
longest = s[0]

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        current += s[i+1]
        if len(current) > max_len:
            max_len = len(current)
            longest = current
    else:
        current = s[i+1]
    i += 1

print('Longest substring in alphabetical order is: ', longest)
