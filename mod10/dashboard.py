import imp
from optparse import Option
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

url = 'spacex_launch_dash.csv'
data = pd.read_csv(url)

df = data[['Payload Mass (kg)','class','Launch Site']].copy()
df.rename(columns = {'Payload Mass (kg)':'Payload', 'Launch Site':'Launch'}, inplace = True)


fig = px.scatter(df,x="Launch",y="Payload",color='class')
fig.update_layout(plot_bgcolor='deepskyblue')


app = dash.Dash(__name__)
app.layout = html.Div(children=[html.Div([html.H1(children="Analytics")]),
    html.Div([  
        fig.show()

    ])])


@app.callback(  [Output(component_id='',component_property='')],
                [Input(component_id='',component_property='')])
def answer(v):
    return -1

if __name__ == "__main__":
    app.run_server(debug=True)