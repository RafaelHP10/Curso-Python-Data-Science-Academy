#Faça um programa que receba um número.
#Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:
	#O número x é impar
#ou
	#O número x é par
#%%

numero = int(input("Digite um numero!"))

resto  = numero % 2

if resto == 0:
    print(f"{numero} é um numero par!")
else:
    print(f"{numero} é um numero impar!")


# %%
