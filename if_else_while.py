#!/usr/bin/env python
# -*- coding: utf-8 -*-


kul_ad="kader"
kul_soyad="tarlan"
while True:
   ad=raw_input(" kullanıcı adı:")
   soyad=raw_input( "kullanıcı soyad:")
   if ad==" " and soyad==" ":
     continue 
   if ad==kul_ad and soyad==kul_soyad:
      print " programa hosgeldınız."
      break
   else:
      print " yanlıs ad soyad"
      break
cevap=raw_input(" sistemden cıkmak mı istiyorsunuz(e/E)")
if 'e' in cevap or 'E' in cevap:
   print "gule gule"
