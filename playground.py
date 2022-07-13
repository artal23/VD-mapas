import pandas as pd
import folium
import webbrowser

from folium.plugins import MarkerCluster
df = pd.read_csv('../service311.csv')
method_group = df.groupby('method_received')

miami = folium.Map(location=[25.947398,-80.273213], zoom_start=10)

for key, group in method_group:
    group_sample = df.sample(100)
    print(key)
    mc_fp = MarkerCluster(icon_create_function=f'''
    function(cluster) {{
        return L.divIcon({{
            html: '<div> <b>' + cluster.getChildCount() + '</b> </div>',
            className: 'leaflet-marker-icon mycluster {key.lower()}-color leaflet-zoom-animated leaflet-interactive',
            iconSize: L.point(40, 40),
        }});
    }}
    ''', maxClusterRadius=150) 

    for row in group_sample.iloc:
        if row['latitude'] != row['latitude']:
            continue
        ticket_id, lati, longi = row[['ticket_id','latitude', 'longitude']]
        mc_fp.add_child(folium.Marker(location=[lati, longi],

         popup=f"""
    <!DOCTYPE html>
<html>
   <head>
      <title>311 sevice</title>
   </head>  
   <body>
      <table border = "3" cellpadding = "5" cellspacing = "5" style="width: 300px;">
         <tr>
         <tr>
            <th style="text-align:center;background-color:#ccccff">Ticket Id:</th>
            <th style="text-align:center;background-color:#ccccff">Calle:</th>
            <th style="text-align:center;background-color:#ccccff">Ciudad:</th>
            <th style="text-align:center;background-color:#ccccff">Metho:</th>
        </tr>
            <td style="text-align:center">{ticket_id}</td>
            <td style="text-align:center">{row['street_address']}</td>
            <td style="text-align:center">{row['city']}</td>
            <td style="text-align:center">{row['method_received']}</td>
           
         </tr>         
      </table>
   </body>  
</html>
    """))
    feature_group = folium.FeatureGroup(name=key)
    mc_fp.add_to(feature_group)
    miami.add_child(feature_group)
    
        # print(ticket_id, lati, longi)
    # print(key, '\n', group[['ticket_id', 'latitude', 'longitude']])

folium.LayerControl(position='topleft').add_to(miami)
miami.get_root().header.add_child(folium.CssLink('./static.css'))

miami.save('mimapa.html')