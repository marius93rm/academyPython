#Verificare se tutti i numeri inseriti in input sono positivi e pari

n_numb=input("Quanti numeri vuoi inserire: ")
flag=0

for i in range(int(n_numb)):
    num=input("Inserisci il numero: ")

    if float(num)%2!=0 or num<0:
        flag=1

if flag==1:
    print("NO")
else:
    print("Tutti positivi e pari")
