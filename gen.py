import pandas as pd
import random

# Crie um dicionário com 100 entradas aleatórias
data = {
    'Número de Quartos': [random.randint(1, 5) for _ in range(100)],
    'Número de Banheiros': [random.randint(1, 4) for _ in range(100)],
    'Número de Garagens': [random.randint(0, 2) for _ in range(100)],
    'Metros Quadrados': [random.randint(50, 200) for _ in range(100)],
    'Número de Encantamento': [random.randint(0, 10) for _ in range(100)],
    'Possui Quadra de Quadribol': [random.choice([1, 0]) for _ in range(100)],
    'Valor de Aluguel': [random.randint(500, 2500) for _ in range(100)],
    'Valor de Venda': [random.randint(50000, 250000) for _ in range(100)]
}

# Crie um DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Salve o DataFrame em um arquivo CSV
df.to_csv('seu_dataset.csv', index=False)