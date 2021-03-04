while True:
    scritto=int(input("Inserire voto prova scritta tra -8 e 8: "))
    pratica=int(input("Inserire voto prova pratica tra 0 e 24: "))
    if scritto>=-8 and scritto<=8 and pratica>=0 and pratica<=24:
        break


flag=True

finale=scritto+pratica

if scritto<=0 or pratica<=0 or finale<18:
    flag=False
if finale>30:
    print("Congratulazioni: 30 e lode")

if flag==True:
    print("Promosso")
else:
    print("Bocciato")
