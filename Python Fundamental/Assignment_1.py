# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:44:02 2019

@author: kjk
"""
#Assignment 1
#problem 2
#defined blanck list l1
l1=[]

#start for lop and give range of no between these paremeter
for i in range(2000,3200):
#if condition for divisible by 7 and not multiple ==of 5
    if (i%7)==0 and (i%5)!=0:
        l1.append(i)
        
        
#problem 2

#take input first name
f=str(input("enter first name"))

#take input lasst name
l=str(input("enter lasst name"))

#concatenate both strings
full_name=(f+" "+l)
#then reverse the full name
reverse_name=full_name[::-1]

#problem3
d=int(input("enter a diameter"))
r=d/2
v=4/3*3.14*r**3
print(v)

#problem 4 add new problem (find simple interest and add in principle amount)
p=int(input("enter a principle amount"))
r=int(input("enter a Interest rate"))
t=int(input("enter a time priode in year"))
si=(p*r*t)/100
total_amount=si+p
print("principle amount=",p)
print("sinple Interest",si)
print("Total amount with interest",total_amount)

#program 5 find Area of a circle using diameter
d=int(input("enter a diameter"))
r=d/2
pi=3.14
area=pi*(r*r)
print("Area of circle=",area)

