#K.Hirv
#17.10.2022
#harjutus04
import random
#tsüklid

#pank
konto = 10000
intress = 0.05
periood = 5

for i in range(periood):
    print(konto,intress*konto,konto+intress*konto)
    konto = round(konto + intress * konto,2)
print(f"Summa kokku: {konto}€")
print(f"Kasum: {round(konto-10000,2)}€")


#arvamismäng
loop = 1

while loop==1:
    arv = random.randint(1,10)
    print(arv) #testimiseks
    for i in range(3):
        pakkumine = int(input("Arva arv 1-10: "))
        if pakkumine==arv:
            print("Juhuu, arvasid ära")
            break
        else:
            print("Paku uuesti")
        loop = int(input("Jätka 1/0: "))
print("Game over")


#viisikud



#korrutustabel
# arv = 5
# for i in range(10):
#     {}{}{arv*i}





#paarisjapaaritu
for i in range(1,10):
    if i%2==0:
        print(f"{i} paaris")
    else:
        print(f"{i} paaritu")





#loto
for i in range(5):
    print(random.randint(0,9), end="")
    
    
    

#tärnid
j=5
for i in range(5):
    print("* " * j)
    j-=1


j=1
for i in range(5):
    print("* " * j)
    j+=1 #suurendab sama muutujat võrra

print()
for i in range(5):
    print("* " * 5)





#müük
hind = "10€"





#juubel
sp = "31.01.2006"
p,k,a = sp.split(".")
vanus = 2022 - int(a)
if vanus%5==0:
    print("On juubel")
else:
    print("Ei ole juubel")



#matemaatika
a,b = 10,20
tehe = input("Vali tehe (+ - * /): ")
if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus = a - b
elif tehe=="*":
    vastus = a * b
elif tehe =="/":
    vastus = a / b
else:
    vastus = "n/a"
print(f"{a} {tehe} {b} = {vastus}")


#ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} teevad kokku ristküliku")


