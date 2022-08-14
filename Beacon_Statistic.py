# In[4]:

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input

url = 'https://raw.githubusercontent.com/aliaazmi/data/main/Data_base_cancer_5_1.csv'
df = pd.read_csv(url)
df.head()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Beacon Hospital Cancer Pt Statistic 2019-2022'),

    dcc.Dropdown(id='year-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.Year.unique())],
                 value='2019', style={'width': '50%'}
                 ),
    dcc.Graph(id='my-graph')
])


@app.callback(
    Output(component_id="my-graph", component_property="figure"),
    Input(component_id="year-choice", component_property="value"),

)
def interactive_graphing(value_year):
    dff = df[df.Year == value_year]
    fig = px.pie(dff, values='Count', names='Cancer',
                 title='Beacon Hospital Cancer Pt Statistic 2019-2022',
                 labels='Cancer')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


if __name__ == '__main__':
    app.run_server()
