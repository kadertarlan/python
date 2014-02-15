#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

yemekadi=""
yemekler=[]

while yemekadi != "tamam":
    yemekadi=raw_input("yemek adını girin:\n (çıkmak için tamam yazın..)")
    yemekler.append(yemekadi)

print "random yemeginiz:", random.choice(yemekler)

