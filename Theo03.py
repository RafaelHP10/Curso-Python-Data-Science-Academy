#%%
contador = 1

while contador <= 15:
    if contador % 2 == 0:
        print(contador)

    contador += 1


#%%

texto = input("Entre com um texto!")

for i in texto:
    if i == 's':
        i = 'x'
    print(i)

#%%
    
seq = range(1,11)

for i in seq:
    print(i)

#%%
for i in range(1,16):
    if i % 2 == 0:
        print(i)

#%%

total = 0
        
while   True:
    valor = input("Digite um valor")

    if valor:
        total += float(valor)

    else:
        print(f"Valor total é {total}")

        break


#%%
palavra = input("Digite uma palavra")

contagem = palavra.count('a')

print(contagem)

#%%

lista = ["Brabinho","Brabo","Brabissimo","Braboneiro","Brabuleta","Brabeza"]
indice = 0

for i in lista:
    print(lista[indice-1:indice+1])
    print(lista[::-1])
    print(lista[::2])
    indice += 1