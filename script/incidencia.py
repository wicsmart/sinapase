import pandas as pd
from pandas.io.json import json_normalize
import json
import sys, os

_path = '/home/wictor/Documentos/aaa.csv'

df = pd.read_csv(_path)

df['data_inicio'] = df['data_inicio'].astype('datetime64[ns]') 


freM = df.groupby(pd.Grouper(key='data_inicio', freq='1M')).sum()


pd.set_option('display.expand_frame_repr', False)
print freM
