######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 15/01/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import L08T2Kirjasto

def main():
    # tulostetaan kirjaston versionumero
    print("Käytetään lämpötilamuunnoskirjaston versiota", L08T2Kirjasto.VERSIO)
    # valikkosilmukka
    while(True):
        # tulostetaan valikon vaihtoehdot
        print("Minkä lämpötilamuunnoksen haluat tehdä?\n1) Celsius->Fahrenheit\n2) Celsius->Kelvin\n3) Fahrenheit->Kelvin\n4) Fahrenheit->Celsius\n5) Kelvin->Celsius\n6) Kelvin->Fahrenheit\n0) Lopeta")
        # valintasyote
        valikko = input("Valintasi: ")
        # jos valinta ei ole lopetus
        if (valikko != "0"):
            # kysytaan muunnettava lampotila
            muunnettava = int(input("Anna lähtölämpötila: "))
        # jos valinta on 1
        if (valikko == "1"):
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.CelsiusFahrenheit(muunnettava)
            # tulostetaan muotoiltu tulos
            print("Lämpötila Fahrenheit asteina:", round(tulos, 2), "\n")
        # jos valinta on 2
        elif (valikko == "2"):
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.CelsiusKelvin(muunnettava)
            # tulostetaan muotoiltu tulos
            print("Lämpötila Kelvin asteina:", round(tulos, 2), "\n")
        # jos valinta on 3
        elif (valikko == "3"):
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.FahrenheitKelvin(muunnettava)
            # tulostetaan muotoiltu tulos
            print("Lämpötila Kelvin asteina:", round(tulos, 2), "\n")
        # jos valinta on 4
        elif (valikko == "4"):
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.FahrenheitCelsius(muunnettava)
            # tulostetaan muotoiltu tulos
            print("Lämpötila Celsius asteina:", round(tulos, 2), "\n")
        # jos valinta on 5
        elif (valikko == "5"):
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.KelvinCelsius(muunnettava)
            # tulostetaan muotoiltu tulos
            print("Lämpötila Celsius asteina:", round(tulos, 2), "\n")
        # jos valinta on 6
        elif (valikko == "6"):
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.KelvinFahrenheit(muunnettava)
            # tulostetaan muotoiltu tulos
            print("Lämpötila Fahrenheit asteina:", round(tulos, 2), "\n")
        else:
           break 
             
    # poistutaan paaohjelmasta
    return None
    
# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
