
#Inserire in una lista "number" numeri della serie di Fibonacci

number=input("Inserire un numero: ")
if number.isnumeric():
    int(number)                       #casting da stringa in input a intero

F=[]                   #creo una lista vuota a cui vado ad aggiungere i numeri
F.append(0)            #della serie di Fibonacci
F.append(1)
for i in range(2, int(number)):
    F.append(F[i-1]+F[i-2])

print(F)
