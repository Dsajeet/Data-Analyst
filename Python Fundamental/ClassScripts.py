# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:52:18 2019

@author: z003u3cr
"""

x = int(input("What's the price: "))
    
# price > 10000 25%
# 10000 > price > 1500    15%
#500< price < 1500  5%
#0%

if x > 10000:
    print(x - x*(0.25))
elif x > 1500 and x <= 1500:
    print(x - x*(0.05))
elif 
else:
    print(x)
    
## Even and odd
    
x = 12
if x % 2 == 0:
    print("even")
else:
    print("odd")


### While loop
while condition:
    # statement

count = 0
x = 1    
while x <= 5:
    print("Acadgild")    
    count = count + 1   
    
    
### For loop
l = [1,2,3]
for i in l:
    print(i)
    print("*******")


## SUm of all elements of the list
l = list(range(10))

for i in l:
    sum_elements = sum_elements + i
    count += 1

    
## break 
## continue
    
## break
for i in l:
    if i <= 5:
        print(i)
    else:
        break

for i in l:
    if i == 6:
        continue
    else:
        print(i)


list(range(1,10, 2))

for i in range(5,10,3):
    print(i)


def function_name(arg1, arg2.....):
    """ Body
    of functions"""

#---------------------------------
def hello_world():
    print("Hello World!!!")

hello_world()


#---------------------------------
def hello_world(Name):
    print("Hello ", Name)

hello_world("Mohit")

#---------------------------------
print("Left", "right")

#---------------------------------
def func_tuple(a,b,c):
    x = a+b
    y = a + b+ c
    z = a*b*c
    return x, y, z

############## Prime Number ############
#    input - Number
#    output - "prime", "not prime"

def prime_or_not(num):
    div = 2
    prime = True
    while div < num:
        if num % div == 0:
            prime = False
            break
        div = div + 1
    
    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

prime_or_not(37)

def Find_Prime(num):
    if num > 1:
       
    else:
       print(num,"is not a prime number")

    
x = 13
if x > 1:
    for i in range(2,x):
        if (x % i) == 0:
            print(x,"is a not a prime number")
            break
    else:
        print(x,"is a prime number")
 
####################################################################
def prime_check(num):
    if num > 2:
        fl = 0
        for i in range(2,2):
            if num % i == 0:
                fl = 1
                break
        if fl == 1:
            print("Not a prime number")
        else:
            print("Prime Number")
    else:
        prime("Please provide number greater than 2")
        
prime_check(2)

## Home work
## 1. Check wether number is armstrong number or not
Armstrong number - 371 = 3**3 + 7**3 + 1**3
def armstrong_check(x):
    "Body"
    
## 2. Factorial 
5! = 5*4*3*2*1
10! = 10*9*8....*1 

def fact(num):
    "Body"
    return factorial(num)
    

## Secure functions
## UDFunctions at one place    
    