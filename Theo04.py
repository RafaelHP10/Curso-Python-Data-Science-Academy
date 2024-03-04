#%%

minha_lista = []

for i in range(0,3):
    item_lista  = input("Digite o item da lista!")
    minha_lista.append(item_lista)

print(minha_lista)

minha_lista.remove("um")

minha_lista.extend(['quatro','cinco'])
minha_lista.extend("testando")

for i in minha_lista:
    print(i.title())

#%%
dados = ['Teo', 'Calvo',31,['Nah','Josefina','Elaina'],['Marina']]

dados[3][-1]

dados[4][0][::2]

#%%

tipo_sorvete = input("Entre com o tipo do sorvete: [casquinha, cascão, cestinha]")
sabor        = input("Entre com o sabor do sorvete: [morango, creme, chocolate]")
cobertura    = input("Entre com a cobertura que você quer: [caramelo, morango, chocolate]")

valor = 0

sorvetes    = {
                "casquinha": 1.00,
                "cascão": 2.5,
                "cestinha": 4.00
}

coberturas  = {
                "caramelo": 1.50,
                "morango": 1.50,
                "chocolate": 1.5,
                "": 0                
}

if tipo_sorvete in sorvetes and cobertura in coberturas:
    valor   += sorvetes[tipo_sorvete]
    valor   += coberturas[cobertura]
    if cobertura == "":
        print(f"O {tipo_sorvete} de {sabor} sem cobertura custa {valor}!")
    else:
        print(f"O {tipo_sorvete} de {sabor} com a cobertura {cobertura} custa {valor}!")
else:
    print("Pedido errado favor pedir novamente!")



