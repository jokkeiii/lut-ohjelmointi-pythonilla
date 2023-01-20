def toistaja(sana, luku):
    for i in range(0, luku):
        print(sana)
sana = ""
while (sana != "lopeta"):
    sana = input("Anna teksti: ")
    
    if (sana != "lopeta"):
        luku = int(input("Anna luku: "))
        toistaja(sana, luku)
        print("")
    else:
        print("Lopetetaan.")

print("Kiitos ohjelman käytöstä.")
