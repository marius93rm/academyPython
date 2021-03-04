#Inserire in input una stringa e un carattere. Vedere quante volte il carattere
#è contenuto nella stringa

stringa=input("Inserisci una stringa: ")
carattere=input("Inserisci un carattere: ")
count=0
for i in range(len(stringa)):
    if stringa[i]==carattere:
        count=count+1
print(count)
