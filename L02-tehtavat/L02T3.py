ekaSana = input("Anna pitkä Sana: ")
print("Antamasi sanan viisi ensimmäistä kirjainta ovat " + ekaSana[0:5])
print("Viisi viimeistä kirjainta ovat " + ekaSana[-5:])
print("Kirjaimet 2,3,4 ja 5 ovat " + ekaSana[1:5:1])

print("\nSanan joka toinen kirjain alkaen toisesta kirjaimesta: " + ekaSana[1::2])

print("\nAnnoit sanan '" + ekaSana + "', joka on takaperin '" + ekaSana[::-1] + "'.\n")

aloitusPaikka = int(input("Anna aloituspaikka: "))
lopetusPaikka = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))
print("Antamillasi asetuksilla sana "+ ekaSana + " tulostuu näin: " + ekaSana[aloitusPaikka:lopetusPaikka:siirtyma])

print("\nSana oli", len(ekaSana), "merkkiä pitkä.")
print("Kiitos ohjelman käytöstä.")