# Ouvre, lis et affecte les valeurs des fichiers total_prix et total_date dans la liste cours

# --> graph du cours
import re

f_prix=open("/home/ubuntu/total_prix.txt", "r")

prix=[]
for l in f_prix:
	prix.append(float(l))

#print(prix)

f_date=open("/home/ubuntu/total_date.txt", "r")
liste=[]

for l in f_date:
	liste.append(l)

newDate=[]
for i in range(len(liste)):
	newDate.append(re.split('\n', liste[i]))


date=[newDate[i][0] for i in range(len(newDate))]
del(date[0])
del(prix[0])

cours = [{
    'y' : prix,
    'x' : date,
    'type' : 'line'
}]

#print(cours)

#Tableau de features

import numpy as np
import pandas as pd
import statistics as st
from datetime import datetime

#defini les horaires d'ouvertures de la bourse et convertion en datetime
now = datetime.now()
start = now.strftime("%d/%m/%Y 09:00:00")
start = datetime.strptime(start, '%d/%m/%Y %H:%M:%S')
end = now.strftime("%d/%m/%Y 17:35:00")
end = datetime.strptime(end, '%d/%m/%Y %H:%M:%S')

bourse=[]
for i in range(len(date)):
	date[i] = datetime.strptime(date[i], '%d/%m/%Y %H:%M:%S')
	if start <= date[i] and date[i] <= end:
		bourse.append(prix[i])

#calcul du low, high, vol, open, close
low=np.min(bourse)
high=np.max(bourse)
vol=np.std(bourse)
open_price=bourse[0]
close_price=bourse[-1]

#convertion en df
features=[['Open',open_price],['Close',close_price],['Volatility',vol],['Low',low],['High',high]]
df = pd.DataFrame(features, columns=['Feature', 'Value'])

#print(df.head())



# DASHBOARD

from dash import Dash, dash_table, dcc, html
import pandas as pd
import numpy as np

app = Dash(__name__)

table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),
    html.H1(children="Affichage du cours de l'action Total Energie"),
    dcc.Graph(figure={'data': cours}),
    html.H1(children='Paramètres de cours'),
    table
])

if __name__ == '__main__':
	app.run_server(debug=True, port=8050)


