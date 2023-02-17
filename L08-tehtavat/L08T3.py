######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 17/01/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

import datetime

def main():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while (True):
        print("Mitä haluat tehdä:\n1) Tunnistaa aika-olion komponentit\n2) Laskea iän päivinä\n3) Tulostaa viikonpäivät\n4) Tulostaa kuukaudet\n0) Lopeta")
        valikko = input("Valintasi: ")
        # jos valinta on 1
        if (valikko == "1"):
            # kutsutaan aliohjelmaa
            AikaOlio()
        # jos valinta on 2
        elif (valikko == "2"):
            # kutsutaan aliohjelmaa
            IkaEro()
        # jos valinta on 3
        elif (valikko == "3"):
            ViikonPaivat()
        # jos valinta on 4
        elif (valikko == "4"):
            Kuukaudet()
        # jos valinta on 0
        elif (valikko == "0"):
            # poistutaan silmukasta
            break
        # jos valintaa ei tunnistettu
        else:
           # tulostetaan virheviesti
           print("Valintaa ei tunnistettu, yritä uudestaan.\n")
    # poistutaan paaohjelmasta
    return None
    

def AikaOlio():
    # kysytaan paivamaara
    pvmStr = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
    pvmObj = datetime.datetime.strptime(pvmStr, "%d.%m.%Y %H:%M")
            # tulostetaan muotoiltu tulos
    print("Annoit vuoden ", pvmObj.year, "\nAnnoit kuukauden ", pvmObj.month, "\nAnnoit päivän ", pvmObj.day, "\nAnnoit tunnin ", pvmObj.hour, "\nAnnoit minuutin ", pvmObj.minute, "\n", sep="")
    # paluu mainiin
    return None
1

def IkaEro():
    # kysytaan paivamaara
    syntymaPaiva = datetime.datetime.strptime(input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: "), "%d.%m.%Y")
    # 
    laskettavaSyntymaPaiva = datetime.date(syntymaPaiva.year, syntymaPaiva.month, syntymaPaiva.day)
    # asetetaan verrattava muuttuja
    kaksTuhatta = datetime.date(2000, 1, 1)
    # kutsutaan aliohjelmaa tekemaan lasku ja asetetaan palautus muuttujaan
    ika = abs(laskettavaSyntymaPaiva - kaksTuhatta)
    # tulostetaan muotoiltu tulos
    print(kaksTuhatta.day, ".", kaksTuhatta.month, ".", kaksTuhatta.year, " sinä olit ", ika.days, " päivää vanha.", "\n", sep="")
    # paluu mainiin
    return None


def ViikonPaivat():
    viikonPaivatObj = datetime.datetime(2023, 2, 13)
    # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
    for index in range(0, 7):
        print(viikonPaivatObj.strftime("%A"))
        viikonPaivatObj = viikonPaivatObj + datetime.timedelta(days=+1)
    # tulostusmuotoilua
    print()
    # paluu mainiin
    return None


def Kuukaudet():
    kuukaudetObj = datetime.datetime(2023, 1, 1)
    # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
    for index in range(0, 12):
        print(kuukaudetObj.strftime("%b"))
        kuukaudetObj = kuukaudetObj + datetime.timedelta(days=+31)
    # tulostusmuotoilua
    print()
    # paluu mainiin
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
