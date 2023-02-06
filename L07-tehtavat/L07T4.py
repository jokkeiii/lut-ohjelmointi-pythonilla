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
    merkki = ""
    hinta = 0

def main():
    # lista olioita varten
    autot = []
    
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    # silmukka valikkoa varten
    while(True):
        # asetetaan valikon palaute valintaan
        valinta = valikko()

        # jos valinta on 1
        if (valinta == 1):
            # kutsutaan aliohjelmaa lisaamaan syotteet listan paikkaan
            autot = syote(autot)
        # jos valinta on 2
        elif (valinta == 2):
            # kutsutaan aliohjelmaa tulostamaan talletetut tiedot
            tulostus(autot)
        # jos valinta on 0
        else:
            # tyhjataan lista ennen lopetusta
            autot.clear()
            # poistutaan silmukasta
            break
        
    # poistutaan paaohjelmasta
    return None
    

def valikko():
    # silmukka valikkoa varten
    while(True):
        print("Käytettävissä olevat toiminnot:\n1) Anna auton tiedot\n2) Tulosta autojen tiedot\n0) Lopeta")
        # kayttajan valinta syotteena
        valinta = int(input("Valintasi: "))
        # jos valinta ei ole 0, 1 tai 2
        if (not(valinta >= 0 and valinta <= 2)):
            # tulostetaan virheviesti ja jatketaan silmukkaa
            print("Tuntematon valinta, yritä uudestaan.")
            # tyhja rivi
            print()
        # jos valinta on ok
        else:
            # poistutaan silmukasta
            break
    # palautetaan valinta
    return valinta

def syote(autot):
    # luodaan olio luokasta
    auto = AUTO()
    # kysytaan syote olion merkkiin
    auto.merkki = input("Anna auton merkki: ")
    # kysytaan syote olion hintaan
    auto.hinta = int(input("Anna auton hinta: "))
    # lisataan olio listaan
    autot.append(auto)
    # tyhja rivi
    print()
    # palautetaan lista
    return autot


def tulostus(autot):
    
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    # silmukka kay lapi listan oliot
    for auto in autot:
        # tulostetaan kunkin olion merkki ja hinta muuttujat
        print(auto.merkki, auto.hinta)
    # tyhja rivi
    print()
    # poistutaan aliohjelmasta
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
