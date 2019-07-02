import pandas as pd
import numpy as np

 
df = pd.read_csv('/home/wictor/NetBeansProjects/sinapase/script/incidencia.csv', sep=';')

df['geopoint'] =  df['latitude'].map(str)+','+df['longitude'].map(str)

del df['latitude']
del df['longitude']

print df

df.to_csv('/home/wictor/NetBeansProjects/sinapase/script/inc.csv', sep = ';', index=False)