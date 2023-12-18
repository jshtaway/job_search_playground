import os
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.io as io
import pandas as pd
from tools import file_ops, convert, parser
from dash import dash_table

reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
jsons = file_ops.load_jsons(reports_dir, output_format = "figure")
report = file_ops.load_json(os.path.join(reports_dir, 'report.json'))
my_parser = parser.Parser()

def graphs():
    divs = []
    for name, figure in jsons.items():
        if "report" in name:
            continue
        divs.append(html.Div([
            html.H4(convert.to_title_string(name)),
            dcc.Graph(id=f"graph-{name}", figure=figure),
        ]))
    return divs


def test_results():
    doDataFrame = True
    if doDataFrame:
        df = my_parser.parse_cucumber_report(report, pd.DataFrame)
        return dash_table.DataTable(
            df.to_dict("records"),
            [
                {"name": i, "id": i}
                for i in df.columns
             ]
        )

    else:
        tests = my_parser.parse_cucumber_report(report, list)
        table_header = html.Thead([
            html.Tr([
                html.Th('Feature'),
                html.Th('Scenario'),
                html.Th('Status'),
                html.Th('Duration')
            ])
        ])
        table_body = html.Tbody([
            html.Tr([
                html.Td(tests[i]['Feature']),
                html.Td(tests[i]['Scenario']),
                html.Td('Passed' if tests[i]['Status'] else 'Failed'),
                html.Td(tests[i]['Duration'])
            ], style={'background-color': '#ADD8E6'}) for i in range(len(tests))
        ])
        return html.Table([table_header, table_body])


if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = html.Div([html.Div(test_results()), html.Div(graphs())])
    app.run_server(debug=True)