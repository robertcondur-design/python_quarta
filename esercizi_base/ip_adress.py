ip = input("Inserisci un indirizzo IP: ")
# .split() è un metodo delle stringhe che suddivide una stringa cercando il carattere separartore SEP
ottetti_str = ip.split(".")
print(ottetti_str)

ottetti = []
for s in ottetti_str:
    ottetti.append(int(s))
print(ottetti)

print(bin(ottetti[2]))

#chiedere il numero di bit, poi un numero binario gestito come stringa, se la lung del num binario inserito è minore 
# del numero di bit aggiungo a sinistra tanti zeri
