#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:43:36 2020

@author: nova
"""
#=========================
## 1 

## (a)

# set a as an empty list
a = []
# extend 1 to 20 to list
a.extend(range(1,21))

##(b)
# reverse results in (a)
a.sort(reverse = True)

## (c)

a = []
a.extend(range(1,21))
b = []
b.extend(range(1,20))
b.sort(reverse = True)
c = a+b

## (d)

a = [4,6,3]
b = 10 * a

## (e)
c = 11*a
del c[-2:]
#=========================

#=========================
## 2
import numpy as np
x = [float(x)/10. for x in list(range(30,61))]

def fn1(x):
    return [np.exp(a)*np.cos(a) for a in x]
    
y = fn1(x)
#=========================
## 3
[2**x/x for x in list(range(1,26))]

#=========================
## 4
a = []
a.extend(range(1,21))
b = []
b.extend(range(1,21))
b.sort(reverse = True)

[a[i] - b[i] for i in range(len(a))]

## 5
import re
ct = 0
with open("lorem.txt") as openfile:
    for line in openfile:
        for word in re.findall(r'\w+', line) :
            if (len(word)<=4 and len(word)>=1 ) :
                #print(word)
                ct +=1
print('The count of length of word between 1 & 4 is %s' % ct)                
ct = 0
with open("lorem.txt") as openfile:
    for line in openfile:
         for word in re.findall(r'\w+', line):
            if len(word)>=8 :
                #print(word)
                ct +=1
print('The count of length of word 8 or greater is %s' % ct) 
ct = 0
with open("lorem.txt") as openfile:
    for line in openfile:
         for word in re.findall(r'\w+', line):
            if len(word)<=7 and len(word)>=4 :
                ct +=1   
print('The count of length of word between 4 & 7 is %s' % ct) 
ct = 0
with open("lorem.txt") as openfile:
    for line in openfile:
        ct = len(re.findall('([A-Z][a-z]+)', line))+ct
print('The count of Capital words between is %s' % ct) 