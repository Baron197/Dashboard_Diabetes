import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
import pickle
from components.diabetesTable import renderTable
from components.scatterPlot import renderScatterPlot
from components.modelPredict import renderModelPredict

loadModel = pickle.load(open('rfc_diabetes.sav', 'rb'))

app = dash.Dash(__name__)

server = app.server

dfDiabetes = pd.read_csv('diabetes.csv')

app.title = 'Dashboard Diabetes'

app.layout = html.Div(children=[
    html.H1(children='Dashboard Diabetes (by Baron P.Hartono)',className='titleDashboard'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Diabetes Dataset', value='tab-1',children=[
            renderTable(dfDiabetes)
        ]),
        dcc.Tab(label='Scatter Plot', value='tab-2',children=[
            renderScatterPlot(dfDiabetes)
        ]),
        dcc.Tab(label='Test Predict', value='tab-3',children=[
            renderModelPredict()
        ]),
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    })
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_graph(pagination_settings, sorting_settings):
    # print(sorting_settings)
    if len(sorting_settings):
        dff = dfDiabetes.head(500).sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = dfDiabetes.head(500)

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

@app.callback(
    Output('outputPredict', 'children'),
    [Input('buttonPredict', 'n_clicks')],
    [State('inputPregnanciesPredict', 'value'), 
    State('inputPlasmaGPredict', 'value'),
    State('inputDiasBloodPredict', 'value'),
    State('inputTricepsPredict', 'value'),
    State('inputSerumPredict', 'value'),
    State('inputBMIPredict', 'value'),
    State('inputPedigreePredict', 'value'),
    State('inputAgePredict', 'value')])
def update_output(n_clicks, pregnancies, plasma, diasblood, triceps, serum, bmi, pedigree, age):
    data = np.array([[pregnancies,plasma,diasblood,triceps,serum,bmi,pedigree,age]])
    prediction = loadModel.predict(data)
    predictProba = loadModel.predict_proba(data)
    hasil = ''
    if(prediction[0] == 1) :
        hasil = 'Diabetic'
    else :
        hasil = 'Normal'
    return 'Prediction : ' + hasil + ' | Probability : ' + str(predictProba[0,1])


if __name__ == '__main__':
    app.run_server(debug=True,port=1997)