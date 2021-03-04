#Determinare il numero più grande

max=None
while True:
    if max==None:
        max=int(input("Inserisci numero: "))
        if max==0:
            break
    else:
        b=int(input("Inserisci numero: " ))
        if b==0:
            break
        if b>max:
            max=b

print(max)


#sum=0
#while True:
#    a=input("Inserisci un numero: ")
#    sum=sum+a
#    if a==0:
#        break



#stringa=input("Inserisci una stringa: ")
#count=0
#for lettera in stringa:
#    if lettera!=" "
#    count=count+1
#print(count)
