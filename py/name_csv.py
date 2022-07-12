import webbrowser

f = open('name_csv.html','w')

mensaje = 'hola mundo'

f.write(mensaje)
f.close()

webbrowser.open('name_csv.html')