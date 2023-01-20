alaRaja = int(input("Anna alueen alaraja: "))
ylaRaja = int(input("Anna alueen yläraja: "))

for i in range(alaRaja, ylaRaja + 1):
   
    if (i % 5 == 0 and i % 7 == 0):
        print("Luku", i,"on jaollinen 5:llä ja 7:llä.")
        print("Lopetetaan etsintä.")
        break
    elif (i % 5 != 0 ):
        print(i, "ei ole jaollinen viidellä, hylätään.")
    elif (i % 7 != 0):
        print(i, "ei ole jaollinen seitsemällä, hylätään.")
    if (i == ylaRaja):
        print("Alueelta ei löytynyt sopivaa arvoa.")

print("Kiitos ohjelman käytöstä.")
