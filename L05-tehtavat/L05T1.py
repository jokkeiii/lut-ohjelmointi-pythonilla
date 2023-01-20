print("Ensimmäinen vaihe:")

def tulostus_funktio():
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")

tulostus_funktio()

print("\nToinen vaihe:")

luku = int(input("Anna luku: "))

print("Päätasolla ennen aliohjelmaa luku on", luku)

def luku_funktio(luku):
    print("Aliohjelmassa parametrin arvo on", luku)
    print("Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen", luku**2)

luku_funktio(luku)

print("Päätasolla aliohjelman jälkeen luku on", luku)

print("\nKolmas vaihe:")

etuNimi = input("Anna etunimi: ")
sukuNimi = input("Anna sukunimi: ")

def nimi_funktio(etuNimi, sukuNimi):
    nimi = etuNimi + " " + sukuNimi
    return nimi

nimi = nimi_funktio(etuNimi, sukuNimi)

print("Etunimi '" + etuNimi + "' ja sukunimi '" + sukuNimi + "' muodostavat nimen '" + nimi + "'.")

print("Kiitos ohjelman käytöstä.")
