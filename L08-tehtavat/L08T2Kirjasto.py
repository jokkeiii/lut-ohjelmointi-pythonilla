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

VERSIO = 1.0

def CelsiusFahrenheit(muunnettava):
    tulos = float(muunnettava * 1.8 + 32)
    # poistutaan paaohjelmasta
    return tulos

def FahrenheitCelsius(muunnettava):
    tulos = float((muunnettava - 32) * (5 / 9))
    # poistutaan paaohjelmasta
    return tulos

def CelsiusKelvin(muunnettava):
    tulos = float(muunnettava + 273.15)
    # poistutaan paaohjelmasta
    return tulos

def KelvinCelsius(muunnettava):
    tulos = float(muunnettava - 273.15)
    # poistutaan paaohjelmasta
    return tulos

def KelvinFahrenheit(muunnettava):
    tulos = float(1.8 * (muunnettava - 273.15) + 32)
    # poistutaan paaohjelmasta
    return tulos

def FahrenheitKelvin(muunnettava):
    tulos = float((5 / 9) * (muunnettava -32) + 273.15)
    # poistutaan paaohjelmasta
    return tulos
