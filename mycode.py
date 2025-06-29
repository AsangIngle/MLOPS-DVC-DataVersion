import pandas as pd
import numpy as np
import os

data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['New york','Los angeles','Chicago']
      }

df=pd.DataFrame(data)
#add new data
new_row_loc={'Name':'gf1','Age':20,'City':'City1'}
df.loc[len(df.index)]=new_row_loc

another_row={'Name':'gf2','Age':22,'City':'City2'}
df.loc[len(df.index)]=another_row
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file  saved to {file_path}")