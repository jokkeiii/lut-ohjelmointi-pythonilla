######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 06/02/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

# otetaan math-kirjasto kayttoon
import math


def main():
    # valikko silmukka
    while(True):
        # tulostetaan valikon vaihtoehdot
        print("Mitä haluat tehdä:\n1) Laskea ympyrän pinta-alan\n2) Arvata luvun\n0) Lopeta")
        # kayttajan syote valintaan
        valinta = int(input("Valintasi: "))
        # jos valinta on 1
        if(valinta == 1):
            # kutsutaan aliohjelmaa laskemaan ympyran pinta-ala
            YmpyranPintaAla()
        # jos valinta on 2
        elif (valinta == 2):
            # kutsutaan ArpaLuku aliohjelmaa
            ArpaLuku()
        # jos valinta on 0
        elif (valinta == 0):
            # poistutaan silmukasta
            break
        # jos valinta ei ole mikaan em.
        else: 
            print("Tuntematon valinta, yritä uudestaan.")

    # poistutaan paaohjelmasta
    return None
    

# aliohjelma kysyy kayttajalta ympyran sateen ja laskee seka tulostaa sen pinta-alan
def YmpyranPintaAla():
    # kayttajan syote ympyran sateelle
    sade = int(input("Anna ympyrän säde kokonaislukuna: "))
    # lasketaan pinta-ala
    pintaAla = math.pi * math.pow(sade, 2)
    # tulostetaan sade ja laskettu pinta-ala
    print("Säteellä", sade, "ympyrän pinta-ala on", round(pintaAla, 2), "\n")
    # poistutaan aliohjelmasta
    return None


def ArpaLuku():
    # asetetaan satunnaisfunktiolle siemenluku
    random.seed(1)
    # arvotaan luku
    arvottuLuku = random()
    # kysytaan arvaus kayttajalta
    print("Arvaa ohjelman arpoma kokonaisluku.")
    arvaus = int(input("Anna kokonaisluku välillä 0-1000: "))
    # laskuri silmukkaa varten
    laskuri = 0
    # silmukka lukujen testausta varten
    while(True):
        # jos arvaus on suurempi kuin arvottu luku
        if (arvaus > arvottuLuku):
            print("Haettu luku on pienempi.")
        elif (arvaus < arvottuLuku):
            print("Haettu luku on suurempi.")
        elif ():
            print()


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
