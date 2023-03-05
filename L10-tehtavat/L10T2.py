######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 05/03/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
import sys


def main():
    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # luettavaTiedostoNimi = "./L10-tehtavat/files/" + luettavaTiedostoNimi
    # listat lukemista varten
    vuosiLuvut = []
    # sanakirja vuosilukuja varten
    vuosiLuvutKirja = {}
    # kutsutaan aliohjelmaa lukemaan tiedosto
    vuosiLuvut = LueTiedosto(luettavaTiedostoNimi)
    # kutsutaan aliohjelmaa analysoimaan tiedot
    vuosiLuvutKirja = AnalysoiTiedot(vuosiLuvut)
    # jos taulukko on tyhja
    if "empty" in vuosiLuvutKirja:
        # poistutaan ohjelmasta
        return None
    # poistutaan paaohjelmasta
    return None


def LueTiedosto(luettavaTiedostoNimi):
    # automerkkien lista
    vuosiLuvut = []
    try:
        # avataan tiedosto luettavaksi
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        # luetaan ensimmainen rivi pois alta 
        rivi = luettavaTiedosto.readline() 
        # silmukka tiedoston lukua varten
        while(True):
            # luetaan rivi
            rivi = luettavaTiedosto.readline() 
            # jos rivi on tyhja
            if (len(rivi) == 0):
                # poistutaan silmukasta
                break
            # poista rivin lopusta rivinvaihto
            rivi = rivi[:-1]
            # muotoillaan teksti taulukoksi
            rivi = rivi.split(";")
            # asetetaan pelkka vuosiluku taulukosta muuttujaksi
            rivi = rivi[1][0:4]
            # lisataan rivi listaan
            vuosiLuvut.append(rivi)
        # suljetaan tiedosto
        luettavaTiedosto.close()
    # jos kasittelyssa tapahtuu virhe
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # poistutaan ohjelmasta
        sys.exit()
    # palautetaan lista
    return vuosiLuvut


def AnalysoiTiedot(vuosiLuvut):
    # kirja johon lisataan automerkit ja niiden maarat
    vuosiLuvutKirja = {}
    # muuttuja autojen yhteismaaralle
    autoMaara = 0
    # jos luettu lista on tyhja
    if (len(vuosiLuvut) == 0):
        # tulostetaan virheviesti
        print("Tiedosto oli tyhjä, yhtään autoa ei tunnistettu.")
        # lisataan "empty" kirjaan
        vuosiLuvutKirja["empty"] = 1
    # jos lista ei ole tyhja
    else:
        # jarjestellaan lista laskevaan jarjestykseen
        vuosiLuvut.sort(reverse=True)
        # kaydaan lista lapi
        for element in vuosiLuvut:
            # jos listan automerkki on jo kirjassa
            if element in vuosiLuvutKirja:
                # lisataan sen arvoon 1
                vuosiLuvutKirja[element] += 1
            # jos ei
            else: 
                # asetetaan se kirjaan arvolla 1
                vuosiLuvutKirja[element] = 1
        # lasketaan autojen maara kirjan arvoista
        for element in vuosiLuvutKirja:
            autoMaara += vuosiLuvutKirja[element]
        print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
        print("Vuosi: Autoja")
        # tulostetaan jokainen kirjan avain ja sen arvo
        for element in vuosiLuvutKirja:
            print("{0}: {1}".format(element, vuosiLuvutKirja[element]))
        # aliohjelman lopetusviesti
        print("Yhteensä", autoMaara, "autoa.")
    # palautetaan kirja
    return vuosiLuvutKirja


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
