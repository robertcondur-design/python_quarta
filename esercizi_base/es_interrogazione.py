a = input("Inserisci una parola:")
a = a.lower()
if a == a[::-1]:
    print("palindroma")
else: 
    print("Non palidroma")