import dash_html_components as html
import dash_table as dt

PAGE_SIZE = 10

def generate_table(dataframe) :
    return dt.DataTable(
        id='table-multicol-sorting',
        columns=[
            {"name": i, "id": i} for i in dataframe.columns
        ],
        pagination_settings={
            'current_page': 0,
            'page_size': PAGE_SIZE
        },
        pagination_mode='be',

        sorting='be',
        sorting_type='multi',
        sorting_settings=[],
        style_table={'overflowX': 'scroll'}
    )

def renderTable(df) :
    return html.Div([
                html.H1('Data Diabetes', className='h1'),
                generate_table(df)
            ])