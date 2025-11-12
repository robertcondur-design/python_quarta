def main():
    mac_adress = input(f"Inserisci il tuo indirizzo MAC: ")
    file = open("./mac-vendors-export.csv", "r")
    righe = file.readlines()
    if righe[k][0:-1] == mac_adress:
        print(f"Il tuo {mac_adress} coincide con {righe[k][0:-1]}")
    else:
        k = k + 1
    file.close()

if __name__ == "__main__":    
    main()
