#Inserire una parola in input e verificare se è palindroma

parola=input("Inserisci una parola: ")

lunghezza=len(parola)
for i in range(lunghezza):
    if parola[i]!=parola[-i-1]:
        print("Non è palindroma")
        break
