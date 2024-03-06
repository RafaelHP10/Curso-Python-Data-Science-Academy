#%%
def valida_entrada():
    while   True :

        try:
            numero = int(input("Entre com um numero de 1 a 15!"))
            
        
        except:
            print("Valor invalido, tente novamente!")
        if 1 <= numero <= 15:
            return numero
        else:
            print("Numero não esta entre 1 e 15, tente novamente!")

numero_sorte = 7

for i in range(3):

    numero  = valida_entrada()

    if numero == numero_sorte:
        print("Acerto miseravi!")
        break
    elif numero > numero_sorte:
        print("Errou! tente um numero menor!")
    else:
        if i == 2:
            print("Errou! Acabou suas chances, tente novamente!")
        else:
            print("Errou! tente um numero maior!")
    