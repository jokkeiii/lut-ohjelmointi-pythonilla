class TietoLuokka:
    tuotekoodi = ""
    tuoteLkm = 0
    tuoteHinta = 0.0


def LueTiedosto(luettavaTiedostoNimi):
    # avataan tiedosto luettavaksi
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    # tuotelista
    tuoteLista = []
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
        # for element in rivi:
        #     print(element)
        # asetetaan tiedot objektiin
        tuoteRivi.tuotekoodi = rivi[0]
        tuoteRivi.tuoteLkm = int(rivi[1])
        tuoteRivi.tuoteHinta = float(rivi[2])
        print(tuoteRivi.tuotekoodi, tuoteRivi.tuoteLkm, tuoteRivi.tuoteHinta)
        # lisataan objekti listaan
        tuoteLista.append(tuoteRivi)
    # for element in tuoteLista:
    #     print(element.tuotekoodi, element.tuoteLkm, element.tuoteHinta)
        
    # suljetaan tiedosto
    luettavaTiedosto.close()
    # aliohjelman lopetusviesti
    print("Tiedosto '", luettavaTiedostoNimi, "' luettu, ", len(tuoteLista), " riviä.", sep="")
    # palautetaan lista
    return tuoteLista


def AnalysoiTiedot(tuoteLista):
    tulosLista = []
    summa = 0
    for element in len(tuoteLista):
        tulos = round(element.tuoteLkm * element.tuoteHinta, 2)
        print("\t",element.tuoteLkm, element.tuoteHinta)
        summa += tulos
        tulos = '{:.2f}'.format(tulos) + "\n"
        tulosLista.append(tulos)
    # aliohjelman lopetusviesti
    print("Tiedot analysoitu, varaston arvo on", summa, "EUR.")
    # palautetaan lista
    return tulosLista


def TallennaTiedot(kirjoitettavaTiedostoNimi, tulosLista):
    # avataan tiedosto kirjoitettavaksi
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    for element in tulosLista:
        # kirjoitetaan tiedot tiedostoon
        kirjoitettavaTiedosto.write(element)
    # suljetaan tiedosto
    kirjoitettavaTiedosto.close()
    # tulostetaan aliohjelman lopetusviesti
    print("Tulokset tallennettu tiedostoon '" + kirjoitettavaTiedostoNimi + "'.")
    return None
