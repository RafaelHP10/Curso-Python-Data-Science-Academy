#%%
import datetime as date

def permanencia(dt_inicio,dt_final):
    dias    = dt_final - dt_inicio
    return dias

data_atual  = date.datetime.today()

print(f"a diferença entre as datas é {permanencia(data_atual,date.datetime(2024,3,20))}")

#%%
def soma(*args):
    total = 0

    for i in args:
        total += i

    return total

soma(1,2,3,4,5,6,7,8,9,10)

#%%
def operacao (op, *num):

    if op == "soma":
        total = 0
        for i in num:
            total += i

    elif op == "mult":
        total = 1
        for i in num:
            total *= i
    
    return total

operacao("mult",1,2,3,4,5,6,7,8,9,10)

#%%
dados = ['Téo','Calvo']

nome, sobrenome = dados

print(nome)
print(sobrenome)

#%%

a = 10
b = 20

print(a,b)
a,b = b,a

print(a,b)