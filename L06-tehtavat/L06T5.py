# aloita kommentointi

def main():

    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna tiedot sisältävän tiedoston nimi: ")

    # lisataan tiedoston eteen sen polku
    luettavaTiedostoNimi = "./L06-tehtavat/files/" + luettavaTiedostoNimi

    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = "L06T5T1.txt"

    # lisataan tiedoston eteen sen polku
    kirjoitettavaTiedostoNimi = "./L06-tehtavat/files/" + kirjoitettavaTiedostoNimi

    # valikon muuttuja
    valinta = 1

    # valikko silmukka
    while (valinta != 0):

        # kutsutaan valikko aliohjelmaa ja asetetaan palautus muuttujaan
        valinta = Valikko()

        # jos valinta on 1
        if (valinta == 1):

            print(luettavaTiedostoNimi + "\n")

            count = 0
            # luetaan luvut
            ekaLuku = LueLuku(luettavaTiedostoNimi, count)
            print("Välissä\n")
            tokaLuku = LueLuku(luettavaTiedostoNimi, count)

            # tulostetaan annetut luvut
            print("Luettiin luvut", ekaLuku, "ja", tokaLuku)

        # jos valinta on 2
        elif (valinta == 2):

            # kutsutaan summa aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Summa(ekaLuku, tokaLuku)

            # kutsutaan aliohjelmaa kirjoittamaan tiedostoon
            KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, kirjoitettavaTeksti)

            # tulostetaan viesti
            print("Tulos tallennettu tiedostoon.")

        # jos valinta on 3
        elif (valinta == 3):

            # kutsutaan osamaara aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Osamaara(ekaLuku, tokaLuku)
            
            # kutsutaan aliohjelmaa kirjoittamaan tiedostoon
            KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, kirjoitettavaTeksti)

            # tulostetaan viesti
            print("Tulos tallennettu tiedostoon.")

        # jos valinta on 0
        elif (valinta == 0):
            # tulostetaan lopetusviesti
            print("Lopetetaan")
        # jos valinta ei ole 1, 2, 3 tai 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")


def Valikko():

    # tulostetaan valinnat    
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    # kysytaan kayttajalta syote
    valikko = int(input("Valitse toiminto (0-3): "))
    # palautetaan kayttajan valinta
    return valikko


def LueLuku(luettavaTiedostoNimi):

    print("Sisällä\n")
    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")

    # luettavaa lukua varten muuttuja
    luettavaLuku = 0

    # silmukka kunnes tiedosto loppuu
    while (True):

        # luetaan rivi tiedostosta ja asetetaan muuttujaan
        rivi = luettavaTiedosto.readline()

        print(rivi, "\tyksi\n")

        # poista rivin lopusta rivinvaihto
        rivi = rivi[:-1]

        print(rivi, "\tkaksi\n")

        # jos rivilla ei ole merkkeja
        if (not(rivi.isdigit())):
            
            # asetetaan luku nollaksi
            luettavaLuku = 0
            # tulostetaan virheviesti
            print("Luvut loppuivat, lopeta ohjelma.")
            # poistutaan silmukasta
            break
        # jos jatkuu
        else:
            
            # asetetaan luku muuttujaan
            luettavaLuku = int(rivi)
            break 
    
    if (count >= 1):
        # suljetaan luettava tiedosto
        luettavaTiedosto.close()

    # palautetaan luettava luku
    return luettavaLuku


def Summa(ekaLuku, tokaLuku):

    # lasketaan lukujen summa ja muotoillaan palautettava lause
    SummaLause = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}"
    # palautetaan SummaLause
    return SummaLause


def Osamaara(ekaLuku, tokaLuku):

    # jos jakaja ei ole nolla
    if (tokaLuku != 0):
        # lasketaan lukujen osamaara ja muotoillaan palautettava lause
        OsamaaraLause = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}"
    # jos jakaja on nolla
    else:
        # asetetaan virhesanoma lauseeksi
        OsamaaraLause = "Nollalla ei voi jakaa."
    
    # palautetaan OsamaaraLause
    return OsamaaraLause


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, kirjoitettavaTeksti):
    
    # avataan kirjoitettava tiedosto muuttujaan
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    
    # kirjoitetaan tiedot tiedostoon
    kirjoitettavaTiedosto.write(kirjoitettavaTeksti)

    # suljetaan tiedosto
    kirjoitettavaTiedosto.close()

    # poistutaan ohjelmasta
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
