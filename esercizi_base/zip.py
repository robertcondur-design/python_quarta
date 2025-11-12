def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 7, 8, 5],
                  [7, 6],
                  [8, 10, 9, 9],
                  [5, 8]]

#voglio stampare il voto affianco di ogni nome

#modificare il codicee sotto per stampare la media di ognuno, stampare il numero di voti per ognuno, stampare il voto massimo e il voto minimo
    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")



if __name__=="__main__":#dunder
    main()