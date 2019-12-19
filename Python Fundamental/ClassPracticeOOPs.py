# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:20:09 2019

@author: z003u3cr
"""

### List Comprehension
l = []
for i in [1,2,3,4]:
    l.append(i**2)
    
## If 
l = [2,5,6,8,10]
x = []
for i in l:
    if i%2 == 0:
        x.append("even")
    else:
        x.append("odd")
        
x = ["even" for i in l if i%2 == 0]
x = ["even" if i%2 == 0 else "odd" for i in l]

lst3 = []
lst4 = []
[lst3.append(i) if i%2==0 else lst4.append(i) for i in [1,2,3,4] ]

## Dictionary Comprehension
x = {"Key1": "Value1",
     "Key2": "Value2"}

{i:i**2 for i in l}
l1 = ["a", "b", "c"]
l2 = [1,2,3]

{"a": 1, "b": 2, "c": 3}

for i in zip(l1, l2):
    print(i[0])
x = {i[0]: i[1] for i in zip(l1, l2)}
