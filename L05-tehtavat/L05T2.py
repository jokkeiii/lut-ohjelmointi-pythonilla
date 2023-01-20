ekaLuku = int(input("Anna ensimmäinen luku: "))
tokaLuku = int(input("Anna toinen luku: "))

def suuruusVertailija(ekaLuku, tokaLuku):
    if (ekaLuku > tokaLuku):
        print("Testatuista luvuista", ekaLuku, "on suurempi kuin", tokaLuku)
        return ekaLuku
    elif (tokaLuku > ekaLuku):
        print("Testatuista luvuista", tokaLuku, "on suurempi kuin", ekaLuku)
        return tokaLuku
    else:
        print("Luvut ovat samansuuruiset.")
        return ekaLuku

isompiLuku = suuruusVertailija(ekaLuku, tokaLuku)

if (isompiLuku == ekaLuku):
    pienempiLuku = tokaLuku
else:
    pienempiLuku = ekaLuku

muuttaja = int(input("Paljonko vähennetään suuremmasta luvusta: "))

erotus = isompiLuku - muuttaja

suuruusVertailija(pienempiLuku, erotus)

print("Kiitos ohjelman käytöstä.")
