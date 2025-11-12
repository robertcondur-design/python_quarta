def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 7, 8, 5],
                  [7, 6],
                  [8, 10, 9, 9],
                  [5, 8]]


#voglio stampare il voto affianco di ogni nome

#modificare il codice sotto per stampare la media di ognuno, stampare il numero di voti per ognuno, stampare il voto massimo e il voto minimo
   
    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")
        media = sum(voto) / len(voto)
        massimo = max(voto) 
        minimo = min(voto)
        print(f"Il massimo è: {massimo}")
        print(f"Il minimo è: {minimo}")
        print(f"La media è: {media}")

        somma = 0
        num_max = lista_voti[0]
        num_min = lista_voti[0]
        for i in voto:
            somma = somma + i
            if num_max<voto:
                num_max = voto
            if num_min>voto:
                num_min = voto
        media = somma / len(voto)

        print(media)
        print(num_max)
        print(num_min)

        

if __name__=="__main__":#dunder
    main()