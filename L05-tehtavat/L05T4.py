MERKKI_MINIMI = 5
MERKKI_MAKSIMI = 15

def main():
    
    sopivaPituus = False
    
    while (not sopivaPituus):
        merkkiJono = merkkiSyote()
        sopivaPituus = syotePituus(merkkiJono)

    return None

def merkkiSyote():
    return input("Anna merkkijono, 5-15 merkkiä: ")   

def syotePituus(merkkiJono):
    
    pituus = 0
    
    for i in merkkiJono:
        pituus += 1

    if (pituus < MERKKI_MINIMI):
        print("Liian lyhyt,", pituus , "merkkiä, anna uusi.")
        return False
    elif (pituus > MERKKI_MAKSIMI):
        print("Liian pitkä,", pituus , "merkkiä, anna uusi.")
        return False
    else:
        print("Annoit sopivan merkkijonon,", pituus, "merkkiä.")
        return True

main()

print("Kiitos ohjelman käytöstä.")
