class TietoLuokka:
    tuotekoodi = ""
    tuoteLkm = 0
    tuoteHinta = 0.0


def LueTiedosto(luettavaTiedostoNimi):
    # avataan tiedosto luettavaksi
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    # objekti
    tuoteRivi = TietoLuokka()
    # silmukka tiedoston lukua varten
    while(True):
        # luetaan rivi
        rivi = luettavaTiedosto.readline()

        # jos rivi on tyhja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        # poistetaan rivinvaihto
        rivi = rivi[:-1]
        # kaytetaan split funktiota hyodyksi joka tekee
        # luetusta rivista listan
        rivi = rivi.split(';')
        # asetetaan tiedot objektiin
        tuoteRivi.tuotekoodi = rivi[0]
        tuoteRivi.tuoteLkm = int(rivi[1])
        tuoteRivi.tuoteHinta = float(rivi[2])

        tulos = '{:.2f}'.format(tuoteRivi.tuoteLkm * tuoteRivi.tuoteHinta)
        tulos = str(tulos) + "\n"
    # suljetaan tiedosto
    luettavaTiedosto.close()
    return None


def AnalysoiTiedot():
    tulos = '{:.2f}'.format(tuoteRivi.tuoteLkm * tuoteRivi.tuoteHinta)
    tulos = str(tulos) + "\n"
    return None


def TallennaTiedot(kirjoitettavaTiedostoNimi):
    # avataan tiedosto kirjoitettavaksi
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    # kirjoitetaan tiedot tiedostoon
    kirjoitettavaTiedosto.write(tulos)
    # suljetaan tiedosto
    kirjoitettavaTiedosto.close()

    return None
