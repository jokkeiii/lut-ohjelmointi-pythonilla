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
import numpy as np
RIVIMAARA = 4
SARAKEMAARA = 4

def main():
    print("Tämä ohjelma esittelee numpy-matriisin käyttöä.")
    print("Matriisi tulostettuna numpy-muotoilulla:")
    matriisi = np.zeros([RIVIMAARA, SARAKEMAARA], int)
    for rivi in range(RIVIMAARA):
        for sarake in range(SARAKEMAARA):
            matriisi[rivi][sarake] = (rivi + 1) * (sarake + 1)
    print(matriisi)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for rivi in range(RIVIMAARA):
        for sarake in range(SARAKEMAARA):
            print(matriisi[rivi][sarake], end=';')
        print()
    print()
    # poistutaan paaohjelmasta
    return None
    
# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
