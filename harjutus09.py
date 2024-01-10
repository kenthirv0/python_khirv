#K.Hirv
#01.11.2022
#hrajutus09
import datetime
import locale

# Tekita tänane kuupäev ning esita kujul 16. June 2016
aeg = datetime.datetime.now()   
print(aeg.strftime("%d. %B.%Y"))

# Kuva eestistatud kuupäev kujul 16. juuni 2016
locale.setlocale(locale.LC_ALL, "et_EE")

print(aeg.strftime("%d. %B %Y"))

# Eralda iskukoodist sünnikuupäev ja leia isiku vanus
ik ="50601310216"
sp = datetime.date(int("20"+ik[1:3]),int(ik[3:5]),int(ik[5:7]))

age = aeg.year - sp.year - ((aeg.month, aeg.day) < (sp.month, sp.day))

print(age)



