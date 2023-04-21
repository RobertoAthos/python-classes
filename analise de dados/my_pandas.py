import pandas as pd

file_path = "https://pycourse.s3.amazonaws.com/temperature.csv"
df = pd.read_csv(file_path)
print(df.head())


# Indexação à análise de dados

# seleção de uma coluna
print('Date:\n', df['temperatura'])

#seleção de múltiplas colunas
print('Date:\n', df[['temperatura', 'date']])

# Selecionar valores das colunas atravez dos índices: iloc/loc
print('todas as linhas da coluna 1:\n', df.iloc[:, 1])
print('todas as linhas da coluna 1:\n', df.loc[:, 'temperatura'])

# indexação por índice de múltiplas colunas
print(df.iloc[:, 1:3])
print(df.loc[:, ['temperatura', 'classification']])

# Indexação booleana

# transformando o tipo da coluna date para datetime
df['date'] = pd.to_datetime(df['date'])

# setando o índice
df = df.set_index('date')
print('Setando o index date para as datas:\n', df)

# seleção de exemplos acima de 25 graus
df[df['temperatura'] >= 25]

# seleção de entradas até Março de 2020
df[df.index <= '2020-03-1']


# Método sort_values, para ordenação do dataframe

# ordernação de forma crescente por uma coluna
print(f'Ordenação da coluna temperatura:\n {df.sort_values(by="temperatura")}')
# ordenação crescente por mais de uma coluna
print(f'Ordenação de 2 colunas:\n {df.sort_values(by=["temperatura", "classification"])}')

# ordenação de forma decrescente por uma coluna: basta adicionaro atributo 'ascending=Flase'

# ordenação crescente pelo index
print('temperatura:',df['temperatura'])