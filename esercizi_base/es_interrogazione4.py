l = ["Ciao", "python", "casa"]
string = ""
for i in l:
    string = string + " " + i
print(string)

string = l[0]
for i in l[1:]:
    string = string + " " + i
print(string)

