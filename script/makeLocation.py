import pandas as pd
import numpy as np

 
df = pd.read_csv('/home/wictor/Documentos/Sinapse/sem_bt.csv', sep=';')

df['geopoint'] =  df['latitude'].map(str)+','+df['longitude'].map(str)

del df['latitude']
del df['longitude']

print df


df.to_csv('/home/wictor/Documentos/Sinapse/incidencia.csv', sep = ';', index=False)