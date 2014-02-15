#!/usr/bin/env python
# -*- coding: utf-8 -*-

print " bu program girdiğiniz sayılar arasından tek ve cift olanları basar.."

s1=int(raw_input("ilk sayiyi girin:"))
s2=int(raw_input("ikinci sayiyi girin:"))

print """ 
    1) tek sayiyi bul..
    2) cift sayiyi bul.."""

tc=raw_input("seciniz..(1-2):")

for i in range(s1,s2):
    if tc== "1":
        if i % 2 == 1:
            print i
    elif tc== "2":
        if i % 2==0:
            print i
    
