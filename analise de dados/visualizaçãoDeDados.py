import pandas as pd
import matplotlib.pyplot as plt

file_path = "https://pycourse.s3.amazonaws.com/temperature.csv"
df = pd.read_csv(file_path)

#plot de linhas // gráfico de linhas para dados numéricos
print(df.plot(figsize=(10, 5), grid=True))

# plot de barras // para dados categóricos
print(df['classification'].value_counts().plot.bar(figsize=(10, 5), rot=0))

# pie plot //  gráfico de pizza
#print(df['classification'].dropna().value_counts().plot.pie(autopct='%1.1f%', shadow=True, figsize=(10, 7)))

plt.show()