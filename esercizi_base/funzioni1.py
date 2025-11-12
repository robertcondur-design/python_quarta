#MODULARITA': suddividere il codice in funzioni.

#costante è una variabile locale
#ATTENZIONE:  costante è accessibile da tutte le funzioni soltanto in lettura
COSTANTE = 3.14

def prima_lettera_maiuscola(stringa):
        '''
        DOCSTRING
        La funzione restituisce stringa con la lettera iniziale maiuscola
        '''
#stringa è una variabile locale
        s = stringa[0].upper() + stringa[1:].lower()
        return s

def media(lista):
     """
     La funzione restituisce la media dei valori presenti in lista e il numero di elementi in lista
     """
     somma = 0.
     n_lista = len (lista)
     for val in lista:
          somma = somma + val

     return somma/n_lista, n_lista

def main():
    print(help(prima_lettera_maiuscola))
    nome = input("Inserisci una parola: ")
    print(prima_lettera_maiuscola(nome))

    voti = [4.5, 10, 8.25, 7, 6]
    m, n = media(voti)
    print(f"La media è {m}, il numero di voti è {n}.")
    if m > 6.:
         print("😊😊😊😊😊😊😊😊😊😊😊")
    else:
         print("😂😂😂😂😂😂😂😂😂😂😂")

if __name__=="__main__":
    main()
