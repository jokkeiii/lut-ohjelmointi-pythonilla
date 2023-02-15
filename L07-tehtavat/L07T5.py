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
    # luettavaTiedostoNimi = "./L07-tehtavat/files/" + luettavaTiedostoNimi
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # kirjoitettavaTiedostoNimi = "./L07-tehtavat/files/" + kirjoitettavaTiedostoNimi

    # luettavien lista
    lukuLista = []
    # kirjoitettavien lista
    tulosLista = []
    # valikon muuttuja
    valinta = 1
    # laskuri lukulistassa etenemistä varten
    lukuLaskuri = 0

    # valikko silmukka
    while (valinta != 0):

        # kutsutaan valikko aliohjelmaa ja asetetaan palautus muuttujaan
        valinta = Valikko()

        # jos valinta on 1
        if (valinta == 1):
            # jos lukuja ei ole viela luettu tiedostosta
            if (lukuLaskuri == 0):
                # luetaan luvut
                lukuLista = LueLuku(luettavaTiedostoNimi)
                # tulostetaan lukuviesti
                # print("Luettu tiedosto '" + luettavaTiedostoNimi[:-11] + "'.")
                # codegrade versio
                print("Luettu tiedosto '" + luettavaTiedostoNimi + "'.")
                # asetetaan luvut laskettaviksi muuttujiin
                ekaLuku = lukuLista[lukuLaskuri]
                tokaLuku = lukuLista[lukuLaskuri + 1]
                # tulostetaan luvut
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                # lisataan laskuriin seuraavia lukuja varten
                lukuLaskuri += 2
            # jos kaikki listan luvut on jo luettu
            elif (lukuLaskuri + 1 > len(lukuLista)):
                print("Luvut loppuivat, lopeta ohjelma.")
            # kun luvut ovat listassa
            else:
                # asetetaan luvut laskettaviksi muuttujiin
                ekaLuku = lukuLista[lukuLaskuri]
                tokaLuku = lukuLista[lukuLaskuri + 1]
                # tulostetaan luvut
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                # lisataan laskuriin seuraavia lukuja varten
                lukuLaskuri += 2
        # jos valinta on 2
        elif (valinta == 2):
            # kutsutaan summa aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Summa(ekaLuku, tokaLuku)
            # lisataan kirjoitettavaTeksti listaan
            tulosLista.append(kirjoitettavaTeksti)
            # tulostetaan viesti
            print("Tulos lisätty listaan.")
        # jos valinta on 3
        elif (valinta == 3):
            # kutsutaan osamaara aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = Osamaara(ekaLuku, tokaLuku)
            # lisataan kirjoitettavaTeksti listaan
            tulosLista.append(kirjoitettavaTeksti)
            # tulostetaan viesti
            print("Tulos lisätty listaan.")

        # jos valinta on 0
        elif (valinta == 0):
            # kutsutaan aliohjelmaa kirjoittamaan listan sisalto tiedostoon
            KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista)
            # tulostetaan lopetusviesti
            # print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi[:-11] + "'.")
            # codegrade versio
            print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi + "'.")
        # jos valinta ei ole 1, 2, 3 tai 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")

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
    # luettavaa lukua varten lista
    luettavatLuvut = []
    
    # silmukka tiedoston lapi kaymiseen
    while (True):
        # luetaan rivi tiedostosta ja asetetaan muuttujaan
        rivi = luettavaTiedosto.readline()
        # poista rivin lopusta rivinvaihto
        rivi = rivi[:-1]
        # jos rivilla ei ole merkkeja
        if (not(rivi.isdigit())):
            # suljetaan tiedosto
            luettavaTiedosto.close()
            # palautetaan luetut luvut
            return luettavatLuvut    
        # jos jatkuu
        else:
            # asetetaan luku listaan
            luettavatLuvut.append(int(rivi))

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


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista):
    # avataan kirjoitettava tiedosto muuttujaan
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    # kirjoitetaan jokainen alkio listasta
    for element in tulosLista:
        # kirjoitetaan tiedot tiedostoon
        kirjoitettavaTiedosto.write(element)
    
    # suljetaan kirjoitettava tiedosto
    kirjoitettavaTiedosto.close()
    # poistutaan ohjelmasta
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
