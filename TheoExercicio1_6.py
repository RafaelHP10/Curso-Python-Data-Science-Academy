#Faça um programa que receba um número em segundos, converta esse número para horas,
#minuto e segundos.
#Exemplos:
#Entrada: 556
#Saída: 0:9:16
#Entrada: 140153
#Saída: 38:55:53

#%%
valor = int(input("Entre com a quantidade de segundos!"))

#def convert(seconds):
    #minuto, segundo = divmod(seconds, 60)
    #hora, minuto    = divmod(minuto, 60)
    #return "%d:%02d:%02d" % (hora,minuto,segundo)

#print(convert(valor))

import datetime 
  
def convert(n): 
    return str(datetime.timedelta(seconds = valor)) 
      

print(convert(valor)) 