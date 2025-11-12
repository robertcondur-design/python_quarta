#in python possiamo delimitare con "" oppure con ''
stringa = "Ciao mondo!"
print(stringa)

#esempio di indicizzazione della stringa
print(f"L'ultimo carattere della stringa è: {stringa[-1]}")

#esempio di slicing delle stringhe
print(f"La sottostringa 2-5 è {stringa[2:5]}.")  #stampa a - o - spazio (indice 2 incluso, 5 escluso)

#assegnazione multipla(vale per ogni tipo di dato)
nome, cognome = "Mario", "Rossi"

#concatenazione tra stringhe
x = nome + ' ' + cognome
print(x)

#?????
y = (nome + ' ') * 10000
print(y)
