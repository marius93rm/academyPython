#Inserire in input un numero positivo N e determinare il massimo intero i tale che
#la somma dei primi i interi sia minore o uguale a N.

N=int(input("Inserire un numero intero positivo: "))

flag=True
i=1
count=0
while flag:
    count=count+i
    if(count+(i+1))>N:
        flag=False
    i=i+1

print(i)
