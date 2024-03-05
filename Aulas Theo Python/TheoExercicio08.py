#%%
#Faça um programa para receber 4 alturas
#Armazene em uma lista e depois mostre a soma dessas alturas.

alturas = []

for i in range(0,int(input("Quantas alturas?"))):
    altura = int(input(f"Entre com a {i+1} altura!"))
    alturas.append(altura)

total   = 0

for j in alturas:
    total += j

print(f"Total 1 é {total}")

total2  = sum(alturas)

print(f"Total 2 é {total2}")

#%%
#Faça um programa que verifique se o item que a pessoa escolheu para comprar
#na loja esta na lista: laranja, cerveja, miojo, carvão, picanha

itens = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']

item_escolhido = input("Entre com o item desejado!")

if item_escolhido in itens:
    print("Item encontrado!")
else:
    print("Item não encontrado!")

#%%
    
dados   = {"Nome":"Téo",
           "Sobrenome":"Calvo",
           "Idade":31,
           "Ex":["Nah","Josefina","Elaine"],
           "Filhos":[{"Nome":"Maria",
                      "Idade":2},
                      {"Nome":"Raul",
                       "Idade":1}]
            }

nome    = dados["Nome"]
filho1  = dados["Filhos"][0]["Idade"]

print(nome)
print(filho1)

dados.keys()

dados.values()

dados.items()
