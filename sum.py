#!/usr/bin/env python
# -*- coding: utf-8 -*-

sayilar=[2,3,2,2,2]
a=1
for i in sayilar:
   a=a*i
print a

b=sum(sayilar)
print b

sayilar2=[1,2,2,3,3]
def carp(liste):
   a=1
   for i in liste:
      a=a*i
   print a

carp(sayilar2)
