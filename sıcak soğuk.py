import random
hs=random.randint(1,101)
tes=0
fark=1
while fark!=0:
    tes=input("1 ile 100 arasinda bir sayi giriniz: ")
    fark2=tes-hs
    if fark2<0:
        fark2=1*fark2
        if fark>fark2:
            print "sicak"
    elif tes==hs:
        print "tebrikler"
        break
    else:
        print "soğuk"
        fark=fark2
