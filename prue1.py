import pandas as pd

#from js import Bokeh, console, JSON
from bokeh.plotting import figure, output_file, show

#from bokeh.embed import json_item
#from bokeh.plotting import figure
#from bokeh.resources import CDN

#from pyodide.http import open_url

#url_content=open_url("https://raw.githubusercontent.com/artal23/Top.Cs.Datos/master/service311.csv")
df = pd.read_csv('service311.csv')#url_content)

array=df['city'].unique()
#array=sorted(array)
Y =df.iloc[:,6]
cont = 0
arr_cont=[]
for j in array:
  for i in Y:
    if(i == j):
      cont = cont +1
  arr_cont.append(cont)
  cont = 0
arr=[0,1,2,3,4,5,6,7,8,9]

p = figure(title = "Bokeh")

print(array)
width = 1

# plotting the bar graph
#p.vbar(arr_cont, top = arr_cont, width=width)
#p.line(array,arr_cont)
p.vbar(arr[0],top=arr_cont[6],width=width,color="violet",legend_label="City_of_Miami_Gardens",muted_alpha=0.2)
p.vbar(arr[1],top=arr_cont[1],width=width,color="green",legend_label="City_of_Hialeah",muted_alpha=0.2)
p.vbar(arr[2],top=arr_cont[9],width=width,color="yellow",legend_label="Miami_Dade_Ccounty",muted_alpha=0.2)
p.vbar(arr[3],top=arr_cont[3],width=width,color="red",legend_label="City_of_Pinecrest",muted_alpha=0.2)
p.vbar(arr[4],top=arr_cont[4],width=width,color="blue",legend_label="City_of_Miami",muted_alpha=0.2)
p.vbar(arr[5],top=arr_cont[5],width=width,color="orange",legend_label="Town_of_Cutler_Bay",muted_alpha=0.2)
p.vbar(arr[6],top=arr_cont[0],width=width,color="brown",legend_label="City_of_Doral",muted_alpha=0.2)
p.vbar(arr[7],top=arr_cont[7],width=width,color="coral",legend_label="City_of_South_Miami",muted_alpha=0.2)
p.vbar(arr[8],top=arr_cont[8],width=width,color="gray",legend_label="Village_of_Palmetto_Bay",muted_alpha=0.2)
p.vbar(arr[9],top=arr_cont[2],width=width,color="gold",legend_label="City_of_North_Miami",muted_alpha=0.2)

p.legend.click_policy="mute"
show(p)
