#Prendere un numero casuale e creare un programma per indovinarlo

import random
numeroRandom=random.randint(1,1000)
flag=True
while flag:
    risposta=int(input("Indovina il numero:"))
    if risposta==numeroRandom:
        print("Bravo")
        flag=False
    elif risposta>numeroRandom:
        print("Il numero è più piccolo")
    elif risposta<numeroRandom:
        print("Il numero è più grande")
