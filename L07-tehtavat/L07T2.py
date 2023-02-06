######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 01/02/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

class AUTO:
    autonMerkki = ""
    autojenLukumaara = 0

def main():
    
    auto1 = AUTO()
    
    auto1 = syote(auto1)

    tulostus(auto1)
    
    # poistutaan paaohjelmasta
    return None


def tulostus(auto1):
    print("Varastossa on nyt " + auto1.autonMerkki + "-merkkisiä autoja", auto1.autojenLukumaara, "kpl.")
    return None


def syote(auto1):
    auto1.autonMerkki = input("Anna automerkki: ")
    auto1.autojenLukumaara = int(input("Anna automerkin lukumäärä varastossa: "))
    return auto1


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
