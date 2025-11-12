#Crea un programma in python che chiede all'utente il suo nome e lo stampa sempre con l'iniziale maiuscola.
parola = input("Dammi il nome: ")
nomeModificato = parola[0].upper() + parola[1:]
print(f"Il nome con l'iniziale maiuscola è: {nomeModificato}")

#Crea un programma in python che chiede all'utente un numero intero e stampa se il numero è divisibile per 2, per 3 o per 5.
#(Hint: usare operatore % per il resto dell divisione)
n = int(input("Dammi un numero intero: "))
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0: 
    print("Il numero è divisibile per 2, 3 o 5")
else:
    print("Il numero NON è divisibile per 2, 3 o 5")

#Crea un programma in python che chiede all'utente una frase e stampi la stringa un carattere si e un carattere no
# (caratteri alternati)
frase = input("Dammi una frase: ")
print(frase[::2])

#Crea un programma in python che chiede all'utente una frase e stampi la stringa al contrario
frase = input("Dammi un frase: ")
print(frase[::-1])