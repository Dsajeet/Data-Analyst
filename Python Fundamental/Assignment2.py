# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:37:39 2019

@author: kjk
"""

"""
1 Write a program which accepts a sequence of comma-separated numbers from console
and generate a list.
"""
n=int(input("enter a no to starting point your list"))
e=int(input("enter a no to ending point your list"))
s=int(input("enter a no to step size in your list"))
l=list(range(n,e,s))
print("my_list=",l)


"""
2. Create the below pattern using nested for loop in Python.
"""
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
        
    print()
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
        
    print()
"""
3 Write a Python program to reverse a word after accepting the input from the user.
"""
user_input=str(input("enter a string "))
print("user_input",user_input)
reverse=user_input[::-1]
print("After revserse",reverse)

"""
4. Write a Python Program to print the given string in the format specified in the
"""
print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN,!\n\t\tSOCIALIST, SECULAR, DEMOCRATIC \n\t\tREPUBLIC and to secure to all its citizens")


"""Probelem 5"""
#write a program to cube sum of first n natural numbers
#mathematcal formula=(n ( n + 1 ) / 2) ^ 2
n=int(input("enter a no"))
sum = 0
for i in range(1, n+1):
    sum +=i*i*i 
    print("sum of cube number",sum)


