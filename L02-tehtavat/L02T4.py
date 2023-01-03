PII = 3.14

ekaLuku = int(input("Anna positiivinen kokonaisluku: "))
print("Luku", ekaLuku, "kerrottuna itsellään on", (ekaLuku*ekaLuku))
sade = int(input("Anna ympyrän säteen pituus kokonaislukuna: "))
keha = 2 * PII * sade
pintaAla = PII * (sade ** 2)
print("Ympyrän säde on ", sade, ", kehä on ", keha, " ja pinta-ala on ", round(pintaAla, 14), ".", sep="")
ekaLuku = int(input("Anna suorakulmion yhden sivun pituus kokonaislukuna: "))
tokaLuku = int(input("Anna suorakulmion toisen sivun pituus kokonaislukuna: "))
keha = ekaLuku * 2 + tokaLuku * 2
pintaAla = ekaLuku * tokaLuku
print("Suorakulmion sivut ovat ", ekaLuku," ja ", tokaLuku, "; kehä on ", keha, "; ja pinta-ala on ", pintaAla, ".", sep="")
print("Kiitos ohjelman käytöstä.")
