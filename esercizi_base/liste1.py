#In python abbiamo le collezioni. Tra le collezioni abbiamo: liste, tuple, dizionari, set.

#vediamo le liste

#creare una lista
l = [3, 3.14, 10, "ciao", True]

#per accedere agli elementi vigono le stesse regole di indicizzazione e slicing delle stringhe
print(f"L'ultimo elemento della lista è: {l[-1]}")
#Si può stampare totalmente una lista 
print(l)
#Tutta la lista senza il primo e l'ultimo elemento
print(f"Tutta la lista senza il primo e l'ultimo elemento: {l[1:-1]}")

#Aggiunta di un elemento
l.append("NUOVO") #Non restituisce nulla ma modifica
print(l)

l.pop() #rimuove l'ultimo elemento della lista 
print(l)

l.append(1) #Non restituisce nulla ma modifica
print(l)