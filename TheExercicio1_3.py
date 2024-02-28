#Faça um programa que receba o raio de uma circunferência em centímetros.
#Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte
#formato.
#Área:  x.xx
#Perímetro:  y.yy
#%%

raio = int(input("Para calcular a area e perimetro da circunferencia, favor informar o raio!"))

area = 3.14 * (raio * raio)
perimetro = 2 * 3.14 * raio

print(f"A area é {area}")
print(f"O perimetro é {perimetro}")
