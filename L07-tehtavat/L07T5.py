######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 14/02/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


def main():

    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    luettavaTiedostoNimi = "./L07-tehtavat/files/" + luettavaTiedostoNimi
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = "L06T5T1.txt"
    # lisataan tiedoston eteen sen polku
    kirjoitettavaTiedostoNimi = "./L07-tehtavat/files/" + kirjoitettavaTiedostoNimi

    # luettavien lista
    lukuLista = []
    # kirjoitettavien lista
    tulosLista = []
    # valikon muuttuja ja laskuri lukulistassa etenemistä varten
    valinta = 1; lukuLaskuri = 0

    # avataan kirjoitettava tiedosto muuttujaan
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")

    # valikko silmukka
    while (valinta != 0):

        # kutsutaan valikko aliohjelmaa ja asetetaan palautus muuttujaan
        valinta = Valikko()

        # jos valinta on 1
        if (valinta == 1):
            if (lukuLaskuri == 0):
                # luetaan luvut
                lukuLista = LueLuku(luettavaTiedostoNimi)
                # tulostetaan annetut luvut
                print("Luettiin luvut", lukuLista)
            else:
                # luetaan luvut listasta
                print(tulosLista[0], tulosLista[1])
        # jos valinta on 2
        elif (valinta == 2):

            # kutsutaan summa aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Summa(a, b)
            # kutsutaan aliohjelmaa kirjoittamaan tiedostoon
            KirjoitaTiedostoon(kirjoitettavaTiedosto, kirjoitettavaTeksti)
            # tulostetaan viesti
            print("Tulos tallennettu tiedostoon.")

        # jos valinta on 3
        elif (valinta == 3):

            # kutsutaan osamaara aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Osamaara(a, b)
            # kutsutaan aliohjelmaa kirjoittamaan tiedostoon
            KirjoitaTiedostoon(kirjoitettavaTiedosto, kirjoitettavaTeksti)
            # tulostetaan viesti
            print("Tulos tallennettu tiedostoon.")

        # jos valinta on 0
        elif (valinta == 0):
            # tulostetaan lopetusviesti
            print("Lopetetaan")
        # jos valinta ei ole 1, 2, 3 tai 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    # palautetaan luettava luku
    luettavaTiedosto.close()
    # suljetaan kirjoitettava tiedosto
    kirjoitettavaTiedosto.close()

    # palautetaan None
    return None


def Valikko():

    # tulostetaan valinnat    
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    # kysytaan kayttajalta syote
    valikko = int(input("Valitse toiminto (0-3): "))
    # palautetaan kayttajan valinta
    return valikko


def LueLuku(luettavaTiedostoNimi):
    
    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    # luettavaa lukua varten muuttuja
    luettavatLuvut = []
    # luetaan rivi tiedostosta ja asetetaan muuttujaan
    rivi = luettavaTiedosto.readline()
    # poista rivin lopusta rivinvaihto
    rivi = rivi[:-1]

    # jos rivilla ei ole merkkeja
    if (not(rivi.isdigit())):
        
        # palautetaan luetut luvut
        return luettavatLuvut
        
    # jos jatkuu
    else:
        
        # asetetaan luku listaan
        luettavatLuvut.append(int(rivi))

    # palautetaan None
    return None    
    
    
def Summa(a, b):

    # lasketaan lukujen summa ja muotoillaan palautettava lause
    SummaLause = f"Summa {a} + {b} = {a + b}\n"
    # palautetaan SummaLause
    return SummaLause


def Osamaara(a, b):

    # jos jakaja ei ole nolla
    #if (b != 0):
    
    # lasketaan lukujen osamaara ja muotoillaan palautettava lause
    OsamaaraLause = f"Osamäärä {a} / {b} = {round((a / b), 2)}\n"
    
    # jos jakaja on nolla
    #else:
    #    # asetetaan virhesanoma lauseeksi
    #    OsamaaraLause = "Nollalla ei voi jakaa."
    
    # palautetaan OsamaaraLause
    return OsamaaraLause


def KirjoitaTiedostoon(kirjoitettavaTiedosto, kirjoitettavaTeksti):
    
    # kirjoitetaan tiedot tiedostoon
    kirjoitettavaTiedosto.write(kirjoitettavaTeksti)
    # poistutaan ohjelmasta
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
