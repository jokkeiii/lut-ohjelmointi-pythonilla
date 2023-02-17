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
            # kysytaan paivamaara
            pvmStr = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            pvmObj = datetime.datetime.strptime(paivamaaraAika, "%d.%m.%Y %H:%M")
            # tulostetaan muotoiltu tulos
            print("Annoit vuoden ", pvmObj.year, "\nAnnoit kuukauden ", pvmObj.month, "\nAnnoit päivän ", pvmObj.day, "\nAnnoit tunnin ", pvmObj.hour, "\nAnnoit minuutin ", pvmObj.minute, "\n", sep="")
        # jos valinta on 2
        elif (valikko == "2"):
            # kysytaan paivamaara
            syntymaPaiva = datetime.datetime.strptime(input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: "), "%d.%m.%Y")
            # asetetaan verrattava muuttuja
            kaksTuhatta =  datetime.date(2000, 1, 1)
            # kutsutaan aliohjelmaa tekemaan lasku ja asetetaan palautus muuttujaan
            ika = syntymaPaiva.day - kaksTuhatta
            # tulostetaan muotoiltu tulos
            print(kaksTuhatta, " sinä olit ", ika.days, " päivää vanha.", "\n", sep="")
        # jos valinta on 3
        elif (valikko == "3"):
            # kysytaan 
            muunnettava = int(input("Anna lähtölämpötila: "))
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.FahrenheitKelvin(muunnettava)
            # tulostetaan muotoiltu tulos
            print()
        # jos valinta on 4
        elif (valikko == "4"):
            # kysytaan muunnettava lampotila
            muunnettava = int(input("Anna lähtölämpötila: "))
            # kutsutaan aliohjelmaa tekemaan muunnos ja asetetaan palautus muuttujaan
            tulos = L08T2Kirjasto.FahrenheitCelsius(muunnettava)
            # tulostetaan muotoiltu tulos
            print()
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
    
# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
