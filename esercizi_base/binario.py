#chiedere il numero di bit, poi un numero binario gestito come stringa, se la lung del num binario inserito è minore 
# del numero di bit aggiungo a sinistra tanti zeri quanti me ne servono

bit = int(input("Inserisci il numero di bit necessari: "))
ip = input("Inserisci un indirizzo IP: ")
if(len(ip)<bit):
    binario = ip + 0*(bit - len(ip))
print(binario)