password = input(" Inserisci la password -> ")
password_blanked = "*" * len(password)
print(f"Hai inseritto la password: {password[0]}{password_blanked[1:]}")
#len prende la lunghezza della stringa