# Importe as bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from flask import Flask, request, jsonify

# Carregue o conjunto de dados a partir de um arquivo CSV
data = pd.read_csv('seu_dataset.csv')

# Defina as features (entradas) e o alvo (valor de aluguel ou venda)
X = data[['Número de Quartos', 'Número de Banheiros', 'Número de Garagens', 'Metros Quadrados', 'Número de Encantamento', 'Possui Quadra de Quadribol']]
y = data[['Valor de Venda', 'Valor de Aluguel']]  # Ou 'Valor de Venda'

# Divida os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Crie e treine um modelo de regressão (você pode usar outros modelos também)
model = LinearRegression()
model.fit(X_train, y_train)

# Defina uma aplicação Flask para criar a API
app = Flask(__name__)

# Crie uma rota para receber entradas em JSON e retornar previsões
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['Número de Quartos'], data['Número de Banheiros'], data['Número de Garagens'], data['Metros Quadrados'], data['Número de Encantamento'], data['Possui Quadra de Quadribol']]
    prediction = model.predict([features])
    venda, aluguel  = prediction[0]

    return jsonify({'Sugestão de Aluguel': aluguel, 'Sugestão de Venda': venda})

if __name__ == '__main__':
    app.run(debug=True)