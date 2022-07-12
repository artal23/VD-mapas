

#LIBRERIAS
import folium
import pandas as pd
import numpy as np

import webbrowser
#import geopandas as gpd
#import shapefile
webbrowser.open('')

from folium.plugins import MarkerCluster #Para agrupar los puntos espaciales o Farmacias
   
size = 1000000
#PUNTOS ESPACIALES
df = pd.read_csv('service311.csv',chunksize=size)

#DEPLOY MAP
miami = folium.Map(location=[25.947398,-80.273213], zoom_start=10)


#Capa de Farmacias

for chunk in df:
    latitude = list(chunk.iloc[:,18])
    longitude = list(chunk.iloc[:,19])
    street= list(chunk.iloc[:,5])
    city= list(chunk.iloc[:,6])
    metodo = list(chunk.iloc[:,20])

'''latitude=df['latitude']
longitude=df['longitude']
street=df['street_address']
distrito=df['neighborhood_district']
'''
print(metodo[0])
mc_fp=MarkerCluster()

for chunk in range(0,300):
    if latitude[chunk]!=latitude[chunk]:
        continue
    else:
        l=latitude[chunk]
        lg=longitude[chunk]
        #text=str(street[lat])+" "+distrito[lat]
        mc_fp.add_child(folium.Marker(location=[l,lg],

         popup=f"""
    <!DOCTYPE html>
<html>
   <head>
      <title>311 sevice</title>
   </head>  
   <body>
      <table border = "3" cellpadding = "5" cellspacing = "5">
         <tr>
         <tr>
            <th style="text-align:center;background-color:#ccccff">Calle:</th>
            <th style="text-align:center;background-color:#ccccff">Ciudad:</th>
            <th style="text-align:center;background-color:#ccccff">Metho:</th>
        </tr>
            <td style="text-align:center">{street[chunk]}</td>
            <td style="text-align:center">{city[chunk]}</td>
            <td style="text-align:center">{metodo[chunk]}</td>
           
         </tr>         
      </table>
   </body>  
</html>
    
    
    """))


        #print(latitude[lat],longitude[lat])
Capa_FP=folium.FeatureGroup(name="df")
mc_fp.add_to(Capa_FP)

miami.add_child(Capa_FP)

#Capas del Mapa Base--------
folium.TileLayer('Stamen Terrain').add_to(miami)
folium.TileLayer('Cartodb Positron').add_to(miami)
folium.TileLayer('CartoDB dark_matter').add_to(miami)
folium.TileLayer('stamentoner').add_to(miami)

folium.LayerControl(position='topleft').add_to(miami)




miami.save('mimapa.html')
webbrowser.open('mimapa.html')