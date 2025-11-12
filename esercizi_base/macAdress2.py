def main():
    file = open("./mac-vendors-export.csv", "r")
    righe = file.readlines()
    file.close()

    mac_adress = []
    vendor = []
    for riga in righe[1:10]:
        campi = riga.split(",")
        mac_adress.append(campi[0])
        vendor.append(campi[1])


    mac = input("Inserisci il MAC adress per intero: ")
    for m, v in zip(mac_adress, vendor):
        if m[0:8]==mac:
            print(f"Il produttore è {v}")






if __name__ == "__main__": 
    main()