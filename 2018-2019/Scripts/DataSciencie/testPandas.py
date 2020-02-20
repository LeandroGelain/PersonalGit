import pandas as pd
import csv
import matplotlib

data =  pd.read_csv('RATEINF-CPI_ITA.csv')
print(data)

graph = matplotlib.subplot(data)
print(graph)