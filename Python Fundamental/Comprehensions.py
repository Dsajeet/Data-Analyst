# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:34:07 2019

@author: z003u3cr
"""

Procedural Programming - 

## Data Cleaning
## Data Modeling
## Evaluate model

top down

OOPs COncept - Object oriented programming Language
# Everything is an object
l = [1,2,3,4,5] - list object
l -> reference variable
l.append()
l.remove()
l.pop()

Class
Object
reference Variable

######################### 
building with 100 floors
plan/map of the building - floor area, 2 BHK, 3BHK, Kitchen 
plan -> any num ber of building
plan is blueprint of the building 

#plan -> Class - properties
#Building -> Object
Object - properties/attributes - Variables
Operations - methods
function/method

#Class - any number of object
## Car
model - softwares - class
Car - Object


list object
class list:
    remove()
    pop()
    append()
    
def 

## Student
class class_name:
    ''' doc_string '''
    
class Student:
    firstname
    lastname
    age
    talk()
    read()
    listen()    

class Student:
    firstname = "Mohit"
    lastname = "Saini"
    age = 30
    
x = Student() ## Creating objects / Instatiation
print("{} {} Age is {}".format(x.firstname, x.lastname, x.age))

###################################################

constructors - __name__
this - java 

class Student:
    def __init__(self, path, lastname, age):
        self.firstname = firstname
        self.lastname = lastname 
        self.age = age
    
    def talk(self):
        print("I'm {} {}".format(self.firstname, self.lastname))
        print(" My age is {}".format(self.age))        
        
Mohit = Student("Mohit", "Saini", 30)
Mohit.firstname = "Rohit"
Lipika = Student("Lip ika", "Kumari", 30)

Mohit.talk()
Lipika.talk()
    
## Data Anaytics/Data Science   
OOPs / 
Procedural

## deploy 
They have to build applications/softwares  

help(sq)
help(Student)

## 
class Doctor:
    ''' Doctor performs treatment '''
    pass
    
# protected, private, public
class encapsulation:
    def __init__(self, public, prot, priv):
        self.public = public
        self._protected = prot
        self.__private = priv

m = encapsulation(10,23,45)  
m.public
    
    
    













