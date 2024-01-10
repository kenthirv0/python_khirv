#K.Hirv
#05.12.23
#harjutus05

#vanused
vanused = [1,11,23,45,56,75]
print(f"Suurim number on {max(vanused)}")
print(f"Väikseim number on {min(vanused)}")
print(f"Keskmine number on {sum(vanused)/len(vanused)}")
print(f"Numbrite summa on {sum(vanused)}")

#duplikaadid
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
uus_opilased = []
for opilane in opilased:
    if opilane not in uus_opilased:
        uus_opilased.append(opilane)
    else:
        opilased.remove(opilane)
print(opilased)



print()


#Õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
#kuva nimed
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1
#kasutaja valib mitmendat muuta INT
nr = int(input("Mitmendat nime muuta tahad?: "))
#kasutaja valib uue nime STRING

#uus nimi lisatakse nimekirja
opilased.append(kasutajavalik, kasutajavalik)
#näita uut nimekirja
print("------------")




#nimede lisamine loendisse
# nimed = []
# for i in range(5):
#     nimed = input("Lisa nimi: ")
#     nimed.append(nimi)
# 
# print(f"Viimane nimi: {nimi}")
# nimed.sort()
# print(nimed)