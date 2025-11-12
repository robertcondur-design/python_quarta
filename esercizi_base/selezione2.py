print("Premi A per inserire")
print("Premi B per inserire")
print("Premi C per cancellare")

tasto = input("-> ")
tasto = tasto.upper()    

if tasto == "A":
    print("L'utente vuole inserire")
elif (tasto == "B"):
    print("L'utente vuole modificare")
elif (tasto == "C"):
    print("L'utente vuole cancellare")
else:
    print("Tato non valido")