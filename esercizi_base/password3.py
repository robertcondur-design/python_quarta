password = input(" Inserisci la password -> ")
password_blanked = password[0] + "*" * (len(password)-2) + password[-1]
print(f"Hai inseritto la password: {password_blanked}")
#len prende la lunghezza della stringa