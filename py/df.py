import folium
import pandas as pd
import numpy as np
from statistics import mode
import matplotlib.pyplot as plt

import webbrowser
#from pyodide.http import open_url
#import geopandas as gpd
#import shapefile
webbrowser.open('')

from folium.plugins import MarkerCluster #Para agrupar los puntos espaciales o Farmacias
   
size = 1000000
#PUNTOS ESPACIALES
df = pd.read_csv('service311.csv',chunksize=size)




#DEPLOY MAP
#miami = folium.Map(location=[25.947398,-80.273213], zoom_start=10)


#Capa de Farmacias

for chunk in df:
    latitude = list(chunk.iloc[:,18])
    longitude = list(chunk.iloc[:,19])
    street= list(chunk.iloc[:,5])
    distrito= list(chunk.iloc[:,6])

'''array=df['neighborhood_district'].unique()

Y =df.iloc[:,9]
cont = 0
arr_cont=[]
for j in array:
  for i in Y:
    if(i == j):
      cont = cont +1
  arr_cont.append(cont)
  cont = 0

plt.plot(array,arr_cont)
plt.ylabel('distritos')
plt.xlabel('Frecuencia')'''
#plt.show()
#f

webbrowser.open('plot1.html')