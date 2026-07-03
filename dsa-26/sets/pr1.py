# Given two lists, find elements common to both using sets.

a = [1,2,3,4]
b = [2,3,4,5]

com = list(set(a)&set(b))
print(com)