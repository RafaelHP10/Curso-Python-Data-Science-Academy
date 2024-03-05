#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

#%%
pedido = int(input("Qual o produto gostaria? Digite 1 para agua mineral e 2 para agua com gas!"))
quantidade = int(input("Quantas unidades gostaria?"))


if pedido == 1: 
    valor = quantidade * 1.5
    if quantidade > 1:
        print(f"{quantidade} aguas minerais são R${valor}!")
    else:
        print(f"{quantidade} agua mineral é R${valor}!")
elif pedido == 2: 
    valor = quantidade * 2.5
    if quantidade > 1:
        print(f"{quantidade} aguas com gaz são R${valor}!")
    else:
        print(f"{quantidade} agua com gaz é R${valor}!")
else:
    print("Valor invalido!")

# %%
