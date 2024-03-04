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