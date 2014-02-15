#!/usr/bin/env python
# -*- coding: utf-8 -*-

sayi=int(raw_input("bir sayi girin. Bende size istediğiniz kuvvetini hesaplayayım:"))

kuvvet=int(raw_input("şimdi de %s sayısının kaçıncı kuvveti istediğini yaz:" %sayi ))
print " %s sayisinin %s. kuvveti %s olur." %(sayi, kuvvet , sayi ** kuvvet)

