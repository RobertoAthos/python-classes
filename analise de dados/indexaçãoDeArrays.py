import numpy as np

# Acessando elementos

x = np.linspace(start=10, stop=100, num=10, dtype=int)
print(x)

# extração de elementos
print('primeiro elemento:', x[0])
print('segundo elemento:', x[1])
print('último elemento:', x[9])
print('último elemento:', x[-1]) # números negativos pega o último valor até o primeiro

# slicing: extração de subarrays
print('dois primerios elementos', x[0:2])
print('dois primerios elementos', x[:2]) # quando o primeiro elemento for 0, necessáriamente não precisa colocar o 0, apenas o :
print('dois úlitmos elementos', x[-2:])

# slicing em arrays 2D
x = x.reshape(2,5) # reshape da variável x anterior para 2 linhas e 5 colunas
print('x:\n', x)

# extrações de elementos bidimensionais
print('primeira linha, segunda coluna:', x[0,1])
print('segunda linha, penúltima coluna:', x[1,-2])
print('última linha, última coluna:', x[1,4])
print('última linha, última coluna:', x[-1,-1])

# slicing: extração de subarrays bidimensionais
print('primeira linha inteira:', x[0,:])
print('primeira linha, segunda à quarta coluna:', x[0,1:4])
print('última coluna inteira:\n', x[:,[-1]])
