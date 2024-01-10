#K.Hirv
#11.10.22
#harjutus02
import math

#kytusekulu
# 400km, 24liitrit

#arvutisüsteemid
#bin hex

#ajateisendus
# täisarvuline jagamine //
# jääk %
minutid = int(input("Sisesta minutid: "))
h = minutid//60
m = minutid%60
print("vastus on:",h,":",m)



#hypotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2)+pow(b,2)),2)
print("Hüpotenuus on",c)


#rulluisutajad
#11,96

#pitsa
hind = 12.90
jootraha = 0.1
inimesi = 3
summa = round((hind+(hind*jootraha))*inimesi,2)
print("Igaüks maksab",summa,"€")


#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind+(hind*ale))*kogus,2)
print(kogus, "Toote hind on",summa,"€")


#kolmnurga ümbermõõt
a,b,c = 30,30,30
p=a+b+c
print("Kolmnurga ümbermõõt on:" ,p)


