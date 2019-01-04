import dash_core_components as dcc
import dash_html_components as html

def renderModelPredict() :
    return html.Div([
                html.H1('Test Predict Diabetes', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('Pregnancies : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputPregnanciesPredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Plasma Glucose : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputPlasmaGPredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Dias Blood Pressure : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputDiasBloodPredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Triceps Thickness : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputTricepsPredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Serum Insulin : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputSerumPredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('BMI : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputBMIPredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Diabetes Pedigree : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputPedigreePredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.P('Age : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputAgePredict', type='number', value='0')
                    ],className='col-4'),
                    html.Div([
                        html.Button('Predict', id='buttonPredict', className='btn btn-primary')
                    ],className='mx-auto', style={ 'paddingTop': '20px', 'paddingBottom': '20px' })
                ],className='row'),
                html.Div([
                    html.H2('', id='outputPredict', className='mx-auto')
                ], className='row')
            ])