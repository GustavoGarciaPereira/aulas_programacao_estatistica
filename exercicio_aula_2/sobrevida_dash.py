# from dash import Dash, dcc, html, Input, Output
# from sklearn.model_selection import train_test_split
# from sklearn import linear_model, tree, neighbors
# from sklearn import metrics, datasets
# import plotly.express as px

# app = Dash(__name__)

# MODELS = {'Logistic Regression': linear_model.LogisticRegression,
#           'Decision Tree': tree.DecisionTreeClassifier,
#           'k-NN': neighbors.KNeighborsClassifier}

# app.layout = html.Div([
#     html.H4("Analysis of the ML model's results using ROC and PR curves"),
#     html.P("Select model:"),
#     dcc.Dropdown(
#         id='dropdown',
#         options=["Logistic Regression", "Decision Tree", "k-NN"],
#         value='Logistic Regression',
#         clearable=False
#     ),
#     dcc.Graph(id="graph"),
# ])


# @app.callback(
#     Output("graph", "figure"), 
#     Input('dropdown', "value"))
# def train_and_display(model_name):
#     X, y = datasets.make_classification( # replace with your own data source
#         n_samples=1500, random_state=0)
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, random_state=42)

#     model = MODELS[model_name]()
#     model.fit(X_train, y_train)

#     y_score = model.predict_proba(X_test)[:, 1]

#     fpr, tpr, thresholds = metrics.roc_curve(y_test, y_score)
#     score = metrics.auc(fpr, tpr)

#     fig = px.area(
#         x=fpr, y=tpr,
#         title=f'ROC Curve (AUC={score:.4f})',
#         labels=dict(
#             x='False Positive Rate', 
#             y='True Positive Rate'))
#     fig.add_shape(
#         type='line', line=dict(dash='dash'),
#         x0=0, x1=1, y0=0, y1=1)

#     return fig


# app.run_server(debug=True)


import dash
from dash import dcc, html
import plotly.graph_objs as go

# Dados iniciais
vivo_no_inicio = 30
dados = [
    {'Tempo': 1, 'N-Censura': 0, 'N-Eventos': 1},
    {'Tempo': 2, 'N-Censura': 0, 'N-Eventos': 3},
    {'Tempo': 3, 'N-Censura': 0, 'N-Eventos': 2},
    {'Tempo': 4, 'N-Censura': 1, 'N-Eventos': 1},
    {'Tempo': 5, 'N-Censura': 0, 'N-Eventos': 7},
    {'Tempo': 10, 'N-Censura': 2, 'N-Eventos': 4},
    {'Tempo': 20, 'N-Censura': 0, 'N-Eventos': 2},
    {'Tempo': 50, 'N-Censura': 0, 'N-Eventos': 1}
]

# Cálculo da sobrevida cumulativa
lista_x, lista_y = [], []
psnfds = 1  # Inicializando com 100% de sobrevida

for i in dados:
    lista_x.append(i['Tempo'])
    morte = i['N-Eventos'] / vivo_no_inicio
    psnfds *= (1 - morte)
    lista_y.append(100 * psnfds)
    vivo_no_inicio -= (i['N-Eventos'] + i['N-Censura'])

# Criar a aplicação Dash
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Sobrevida Kaplan-Meier"),
    dcc.Graph(
        id='sobrevida-plot',
        figure={
            'data': [
                go.Scatter(
                    x=lista_x,
                    y=lista_y,
                    mode='lines+markers',
                    name='Sobrevida',
                    line_shape='hv'
                )
            ],
            'layout': {
                'title': 'Gráfico de Sobrevida',
                'xaxis': {
                    'title': 'Tempo'
                },
                'yaxis': {
                    'title': 'Probabilidade de Sobrevida (%)'
                },
                'showlegend': True
            }
        }
    )
])

# if __name__ == '__main__':

#     # server = app.server

#     # @server.after_request
#     # def add_custom_header(response):
#     #     response.headers['ngrok-skip-browser-warning'] = "1"
#     #     return response

# app.run_server(debug=True)
