import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# Classificação de padrões no scikit-learn
# mini programa de predição de temperaturas

file_path = "https://pycourse.s3.amazonaws.com/temperature.csv"
df = pd.read_csv(file_path)

# valores
x, y = df[['temperatura']].values, df[['classification']].values

# pré-processamento
# conversão de y para valores numéricos
le = LabelEncoder()
y = le.fit_transform(y.ravel()) # faz o calculo dos parametros recebidos do input
#print(y)

clf = LogisticRegression() # modelo de classificação, que vai descriminar da melhor maneira as classes
clf.fit(x, y)

"""""
Gerando 100 valores de temperatura linearmente espaçados entre 0 e 45,
vai fazer uma predição em novos valores de temperatura
"""
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# predição desses valores
y_pred = clf.predict(x_test)
#print(y_pred) # vai imprimir números pois a gente converteu o y para números acima para realizar os cálculos

# conversão de y_pred para os valores originais
y_pred = le.inverse_transform(y_pred)
#print(y_pred)

# output
output = {'new_temp': x_test.ravel(),
          'new_class': y_pred.ravel()}
output = pd.DataFrame(output)

def classify_temp():
    ask = True
    while ask:
        # input de temperatura
        temp = input('Insira a temperatura (graus celsius):')
        # transformar para numpy array
        temp = np.array(float(temp)).reshape(-1,1)
        # realiza classificação
        class_temp = clf.predict(temp)
        # transformação inversa para retornar string original
        class_temp = le.inverse_transform(class_temp)
        # classificação
        print(f'A classificação da temperatura {temp.ravel()[0]} é:', class_temp[0])

        #perguntar
        ask = input('Nova classificação (y/n): ') == 'y'

classify_temp()
