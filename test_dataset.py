from bcb import sgs
import pandas as pd

codigos = {
    'IC-Br Total': 27574,        
    'IC-Br Agro': 27575,        
    'IC-Br Metal': 27576,        
    'IC-Br Energia': 27577,        
}

df_commodities = sgs.get(codigos, start='2010-01-01')

# print(df_commodities.head())

df_commodities.to_csv('ic_br_historico.csv')
