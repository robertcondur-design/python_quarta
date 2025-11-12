file = open("./dati.csv", "r") #oggetto file
righe = file.readlines() #liste di stringhe che contiene le righe del file
file.close()

print(righe)
print(righe[0])
titoli = righe[0][:-1].split(",")
print(titoli)

prima_riga = righe[0]
#unpacking (=spacchettamento)
titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")
print(titolo1)
print(titolo2[1:])
print(titolo3[1:])



