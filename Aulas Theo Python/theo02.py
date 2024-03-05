#%%
from datetime import date

data_atual = date.today()

aniversario = input("É seu aniversario? digite 'S' ou 'N'!")

if aniversario == 'S':
    print("Feliz aniversario!")
else:
    mes = int(input("Digite o mes do seu aniversario!"))
    dia = int(input("Digite o dia do seu aniversario!"))
    aniversario = date(data_atual.year, mes, dia)
    if aniversario < data_atual:
        aniversario = aniversario.replace(year=data_atual.year + 1)
        dias_niver = abs(aniversario - data_atual)
        print(f"Faltam {dias_niver.days} para o seu aniversario")
    else:
        dias_niver = abs(aniversario - data_atual)
        print(f"Faltam {dias_niver.days} para o seu aniversario")