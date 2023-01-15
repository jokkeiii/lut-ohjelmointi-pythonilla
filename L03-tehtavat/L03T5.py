pituus = int(input("Anna pituus (cm): "))

paino = int(input("Anna paino (kg): "))

bmi = round(paino / (pituus / 100)**2, 1)

if (bmi <= 17):
    bmiSana = "(Vaarallinen aliravitsemus)"
elif (bmi > 17 and bmi < 18.5):
    bmiSana = "(Liiallinen laihuus)"
elif (bmi >= 18.5 and bmi < 25):
    bmiSana = "(Normaali paino)"
elif (bmi >= 25 and bmi < 30):
    bmiSana = "(Ylipaino)"
elif (bmi >= 30 and bmi < 35):
    bmiSana = "(Merkittävä lihavuus)"
elif (bmi >= 35 and bmi < 40):
    bmiSana = "(Vaikea lihavuus)"
else:
    bmiSana = "(Sairaalloinen lihavuus)"

print("Painoindeksi on", bmi, bmiSana)

tavoiteIndeksi = float(input("Anna tavoiteindeksi: "))

tavoitePaino = round(tavoiteIndeksi * (pituus/100)**2, 1)

if (tavoiteIndeksi < bmi):
    tavoitePainoErotus = round(paino - tavoitePaino, 1)
    isoTaiPieni = "alhaisempaa"
else:
    tavoitePainoErotus = round(tavoitePaino - paino, 1)
    isoTaiPieni = "suurempaa"

print("Tavoiteindeksi vastaa", tavoitePainoErotus, "kg", isoTaiPieni , "painoa.")

print("Kiitos ohjelman käytöstä.")
