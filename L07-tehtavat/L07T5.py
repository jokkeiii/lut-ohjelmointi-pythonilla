######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 11/02/2023
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

    # valikon muuttuja
    valinta = 1

    # avataan kirjoitettava tiedosto muuttujaan
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")

    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")

    # valikko silmukka
    while (valinta != 0):

        # kutsutaan valikko aliohjelmaa ja asetetaan palautus muuttujaan
        valinta = Valikko()

        # jos valinta on 1
        if (valinta == 1):

            # luetaan luvut
            ekaLuku = LueLuku(luettavaTiedostoNimi, luettavaTiedosto)
            tokaLuku = LueLuku(luettavaTiedostoNimi, luettavaTiedosto)

            # tulostetaan annetut luvut
            print("Luettiin luvut", ekaLuku, "ja", tokaLuku)

        # jos valinta on 2
        elif (valinta == 2):

            # kutsutaan summa aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Summa(ekaLuku, tokaLuku)

            # kutsutaan aliohjelmaa kirjoittamaan tiedostoon
            KirjoitaTiedostoon(kirjoitettavaTiedosto, kirjoitettavaTeksti)

            # tulostetaan viesti
            print("Tulos tallennettu tiedostoon.")

        # jos valinta on 3
        elif (valinta == 3):

            # kutsutaan osamaara aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Osamaara(ekaLuku, tokaLuku)
            
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


def LueLuku(luettavaTiedostoNimi, luettavaTiedosto):

    # luettavaa lukua varten muuttuja
    luettavaLuku = 0

    # luetaan rivi tiedostosta ja asetetaan muuttujaan
    rivi = luettavaTiedosto.readline()

    # poista rivin lopusta rivinvaihto
    rivi = rivi[:-1]

    # jos rivilla ei ole merkkeja
    if (not(rivi.isdigit())):
        
        # asetetaan luku nollaksi
        luettavaLuku = 0
        # tulostetaan virheviesti
        print("Luvut loppuivat, lopeta ohjelma.")
        
        # palautetaan luettava luku
        return luettavaLuku
        
    # jos jatkuu
    else:
        
        # asetetaan luku muuttujaan
        luettavaLuku = int(rivi)
        # palautetaan luettava luku
        return luettavaLuku 

    # palautetaan None
    return None    
    
    
def Summa(ekaLuku, tokaLuku):

    # lasketaan lukujen summa ja muotoillaan palautettava lause
    SummaLause = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}\n"
    # palautetaan SummaLause
    return SummaLause


def Osamaara(ekaLuku, tokaLuku):

    # jos jakaja ei ole nolla
    #if (tokaLuku != 0):
    
    # lasketaan lukujen osamaara ja muotoillaan palautettava lause
    OsamaaraLause = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}\n"
    
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
