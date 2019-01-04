import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

color_set = ['#80aaff','#cc0000']

def legendDiabetic(val) :
    if(val == 1) :
        return 'Diabetic'
    
    return 'Normal'

def renderScatterPlot(df) :
    return html.Div([
                html.H1('Scatter Plot Diabetes', className='h1'),
                dcc.Graph(
                    id='scatterPlot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df[df['Diabetic'] == col].head(500)['Age'],
                                y=df[df['Diabetic'] == col].head(500)['PlasmaGlucose'],
                                mode='markers',
                                marker=dict(color=color_set[i], size=10, line=dict(width=0.5, color='white')),
                                name=legendDiabetic(col)
                            ) for col, i in zip(df['Diabetic'].unique(), range(2))
                        ],
                        'layout': go.Layout(
                            xaxis= dict(title='Age'),
                            yaxis={'title': 'Plasma Glucose'},
                            margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
                            hovermode='closest'
                        )
                    }
                )
            ])