######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 03/03/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


def main():
    naytaValikko = True
    while (True):
        if (naytaValikko):
            # tulostetaan valinnat    
            print("Mitä haluat tehdä:\n1) Testaa ValueError\n2) Testaa IndexError\n3) Testaa ZeroDivisionError\n4) Testaa TypeError\n0) Lopeta")
        
        try:
            # kysytaan kayttajalta syote
            valinta = int(input("Valintasi: "))
            naytaValikko = True
            # valintatestit
            if (valinta == 1):
                print("Valikko-ohjelma testaa ValueError'n.")
            # jos valinta on 2
            elif (valinta == 2):
                # kutsutaan aliohjelmaa testaamaan kyseinen virhetapaus
                TestaaIndexError()
            # jos valinta on 3
            elif (valinta == 3):
                # kutsutaan aliohjelmaa testaamaan kyseinen virhetapaus
                TestaaZeroDivisionError()
            # jos valinta on 4
            elif (valinta == 4):
                # kutsutaan aliohjelmaa testaamaan kyseinen virhetapaus
                TestaaTypeError()
            # jos valinta on 0
            elif (valinta == 0):
                break
            # jos valinta ei ole 1, 2, 3 tai 0
            else:
                print("Valintaa ei tunnistettu, yritä uudestaan.")
        except ValueError:
            print("Anna valinta kokonaislukuna.")
            naytaValikko = False
    # poistutaan paaohjelmasta
    return None


def TestaaIndexError():
    lista = [11, 22, 33, 44, 55]
    syote = int(input("Anna indeksi 0-4: "))
    try:
        print("Listan arvo on ", lista[syote], " indeksillä ", syote, ".", sep="")
    except IndexError:
        print("Tuli IndexError, indeksi ", syote, ".", sep="")
    return None


def TestaaZeroDivisionError():
    syote = int(input("Anna jakaja: "))
    try:
        print("4/2 on ", '{:.2f}'.format(4/syote), ".", sep="")
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja ", syote, ".", sep="")
    return None

   
def TestaaTypeError():
    syote = input("Anna numero: ")
    try:
        print(syote*syote)
    except TypeError:
        print("Tuli TypeError, ", syote, "*", syote, " merkkijonoilla ei onnistunut.", sep="")
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
