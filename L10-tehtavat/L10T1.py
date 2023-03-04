######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 04/03/2023
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
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # kirjoitettavaTiedostoNimi = "./L10-tehtavat/files/" + kirjoitettavaTiedostoNimi
    # listat lukemista ja tallenntamista varten
    autoMerkit = []
    eriAutoMerkit = []
    # sanakirjat lukemista ja tallentamista varten
    autoMerkitKirja = {}
    # kutsutaan aliohjelmaa lukemaan tiedosto
    autoMerkit = LueTiedosto(luettavaTiedostoNimi)
    # kutsutaan aliohjelmaa analysoimaan tiedot
    autoMerkitKirja = AnalysoiTiedot(autoMerkit)
    # jos taulukko on tyhja
    if "empty" in autoMerkitKirja:
        # poistutaan ohjelmasta
        return None
    # kutsutaan aliohjelmaa tallentamaan analysoidut tiedot
    TallennaTiedot(kirjoitettavaTiedostoNimi, autoMerkitKirja)

    # poistutaan paaohjelmasta
    return None


def LueTiedosto(luettavaTiedostoNimi):
    # automerkkien lista
    autoMerkit = []
    try:
        # avataan tiedosto luettavaksi
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
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
            # lisataan rivi listaan
            autoMerkit.append(rivi)
        # suljetaan tiedosto
        luettavaTiedosto.close()
    # jos kasittelyssa tapahtuu virhe
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # poistutaan ohjelmasta
        sys.exit()
    # palautetaan lista
    return autoMerkit


def AnalysoiTiedot(autoMerkit):
    # kirja johon lisataan automerkit ja niiden maarat
    autoMerkitKirja = {}
    # muuttuja autojen yhteismaaralle
    autoMaara = 0
    # jos luettu lista on tyhja
    if (len(autoMerkit) == 0):
        # tulostetaan virheviesti
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
        # lisataan "empty" kirjaan
        autoMerkitKirja["empty"] = 1
    # jos lista ei ole tyhja
    else:
        # kaydaan lista lapi
        for element in autoMerkit:
            # jos listan automerkki on jo kirjassa
            if element in autoMerkitKirja:
                # lisataan sen arvoon 1
                autoMerkitKirja[element] += 1
            # jos ei
            else: 
                # asetetaan se kirjaan arvolla 1
                autoMerkitKirja[element] = 1
        # lasketaan autojen maara kirjan arvoista
        for element in autoMerkitKirja:
            autoMaara += autoMerkitKirja[element]
        # aliohjelman lopetusviesti
        print("Tunnistettiin", len(autoMerkitKirja), "automerkkiä ja", autoMaara, "autoa:")
        # tulostetaan jokainen listan jasen
        for element in autoMerkitKirja:
            if (autoMerkitKirja[element] == 1):
                print("{0}: {1} auto".format(element, autoMerkitKirja[element]))
            else:
                print("{0}: {1} autoa".format(element, autoMerkitKirja[element]))
    # palautetaan lista
    return autoMerkitKirja


def TallennaTiedot(kirjoitettavaTiedostoNimi, autoMerkitKirja):
    # muuttuja autojen yhteismaaralle
    autoMaara = 0
    # muuttuja virheentarkastusta varten
    virhe = False
    try:
        # avataan tiedosto kirjoitettavaksi
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        # lasketaan autojen maara kirjan arvoista
        for element in autoMerkitKirja:
            autoMaara += autoMerkitKirja[element]
        # aliohjelman lopetusviesti
        kirjoitettavaTiedosto.write("Tunnistettiin {0} automerkkiä ja {1} autoa:\n".format(len(autoMerkitKirja), autoMaara))
        # kaydaan jokainen kirjan kohta lapi
        for element in autoMerkitKirja:
            # kirjoitetaan tiedot tiedostoon
            if (autoMerkitKirja[element] == 1):
                kirjoitettavaTiedosto.write("{0}: {1} auto\n".format(element, autoMerkitKirja[element]))
            else:
                kirjoitettavaTiedosto.write("{0}: {1} autoa\n".format(element, autoMerkitKirja[element]))
        # suljetaan tiedosto
        kirjoitettavaTiedosto.close()
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # poistutaan ohjelmasta
        sys.exit()
    # palautetaan virhemuuttuja
    return virhe


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
