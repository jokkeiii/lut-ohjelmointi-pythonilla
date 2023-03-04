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
    # luettavaTiedostoNimi = "./L09-tehtavat/files/" + luettavaTiedostoNimi
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # kirjoitettavaTiedostoNimi = "./L09-tehtavat/files/" + kirjoitettavaTiedostoNimi
    # listat lukemista ja tallenntamista varten
    autoMerkit = []
    eriAutoMerkit = []
    # kutsutaan aliohjelmaa lukemaan tiedosto
    autoMerkit = LueTiedosto(luettavaTiedostoNimi)
    # jos kasittelyssa virhe
    if "stop" in autoMerkit:
        # poistutaan ohjelmasta
        sys.exit()
    # kutsutaan aliohjelmaa analysoimaan tiedot
    eriAutoMerkit = AnalysoiTiedot(autoMerkit)
    # jos kasittelyssa virhe
    if "empty" in eriAutoMerkit:
        # poistutaan ohjelmasta
        return None
    # kutsutaan aliohjelmaa tallentamaan analysoidut tiedot
    virhe = TallennaTiedot(kirjoitettavaTiedostoNimi, eriAutoMerkit)
    # jos kasittelyssa virhe
    if (virhe == True):
        # poistutaan ohjelmasta
        sys.exit()

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
            # lisataan rivi listaan
            autoMerkit.append(rivi)
        # suljetaan tiedosto
        luettavaTiedosto.close()
    # jos kasittelyssa tapahtuu virhe
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # ja lisataan stop listaan
        autoMerkit.append("stop")
    # palautetaan lista
    return autoMerkit


def AnalysoiTiedot(autoMerkit):
    # lista johon lisataan vain yksi kutakin automerkkia
    eriAutoMerkit = []
    # jos luettu lista on tyhja
    if (len(autoMerkit) == 0):
        # tulostetaan virheviesti
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
        # lisataan stop listaan
        eriAutoMerkit.append("empty")
    else:
        # jos lista ei ole tyhja
        for element in autoMerkit:
            # tarkistetaan onko kyseinen element jo uudessa listassa
            if element not in eriAutoMerkit:
                # jos ei lisataan se uuteen listaan
                eriAutoMerkit.append(element)
        # aliohjelman lopetusviesti
        print("Tiedostossa oli", len(eriAutoMerkit), "eri automerkkiä.")
        # tulostetaan jokainen listan jasen
        for element in eriAutoMerkit:
            print(element, end="")
    # palautetaan lista
    return eriAutoMerkit


def TallennaTiedot(kirjoitettavaTiedostoNimi, eriAutoMerkit):
    # muuttuja virheentarkastusta varten
    virhe = False
    try:
        # avataan tiedosto kirjoitettavaksi
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        # kaydaan jokainen listan kohta lapi
        for element in eriAutoMerkit:
            # kirjoitetaan tiedot tiedostoon
            kirjoitettavaTiedosto.write(element)
        # suljetaan tiedosto
        kirjoitettavaTiedosto.close()
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # ja asetetaan virhe todeksi
        virhe = True
    # palautetaan virhemuuttuja
    return virhe


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
