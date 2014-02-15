#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cift(sayi):
  print sayi," bu sayi cifttir."
def tek(sayi):
  print sayi, " bu sayi tektir."

sayi=int(raw_input("bir sayi gir:"))
if(sayi%2==0):
  cift(sayi)
else:
  tek(sayi)
cift(6)
tek(7)
