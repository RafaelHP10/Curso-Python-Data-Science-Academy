#%%
numero_sorte    = 7




while True:
    try:
 
        numero = int(input("Entre com um numero entre 1 e 15!"))
    
        if numero <= 0 and numero > 15:
            continua = print("Valor invalido! Deseja continuar! [sim,não]")
            if continua == 'sim':
                pass
            else:
                print("Mais sorte na próxima vez!")
                break
        else:
            if numero != numero_sorte:
                continua = input("Errou! Deseja continuar! [sim,não]")
                if continua == 'sim':
                    pass
                else:
                    print("Mais sorte na próxima vez!")
                    break
            else:
                print("Acerto miseravi!")
                break

    except:
        print("Valor invalido tente novamente!")
        pass
