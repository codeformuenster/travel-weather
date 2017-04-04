## CONVERTING CSVs https://data.giss.nasa.gov TO JSON

import pandas as pd
import os

#%% SCRIPT PARAMETERS

folder_in = '../data/csv/'
folder_out = '../data/json/'

#%% load CSV

file_in = 'station.csv'
df = pd.read_csv(os.path.join(folder_in, file_in))

#%% PROCESS?


#%% WRITE AS JSON TO FILE

file_out = 'station.json'
df.to_json(os.path.join(folder_out, file_out))