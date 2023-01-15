ekaSana = input("Anna sana 1: ")
tokaSana = input("Anna sana 2: ")

if (ekaSana < tokaSana):
    print("'" + ekaSana + "' on aakkosissa aiemmin kuin '" + tokaSana + "'.")
elif (ekaSana > tokaSana): 
    print("'" + tokaSana + "' on aakkosissa aiemmin kuin '" + ekaSana + "'.")
else:
    print("Sanat ovat samoja.")
if ('z' in ekaSana):
    print("Kirjain 'z' löytyy sanasta 1.")
if ('z' in tokaSana):
    print("Kirjain 'z' löytyy sanasta 2.")
if (not('z' in ekaSana or 'z' in tokaSana)):
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

testiSana = input("Anna testattava sana: ")

if (testiSana == testiSana[::-1]):
    print("Antamasi sana '" + testiSana + "' on palindromi.")
else:
    print("Antamasi sana ei ole palindromi.")
    print("Se on väärinpäin '" + testiSana[::-1] + "' ja oikein päin '" + testiSana + "'.")

print("Kiitos ohjelman käytöstä.")
