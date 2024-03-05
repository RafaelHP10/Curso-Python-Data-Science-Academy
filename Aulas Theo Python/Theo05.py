#%%

import datetime as date

def permanencia(dt_inicio,dt_final):
    dias    = abs(dt_inicio - dt_final)
    return dias

print(f"a diferença entre as datas é {permanencia(date.datetime(2024,3,20),date.datetime(2024,3,4))}")
