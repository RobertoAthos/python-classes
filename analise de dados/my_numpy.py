import numpy as np
# lib de visualização de dados
import matplotlib.pyplot as plt

x = np.array([[1, 3, 7],[4, 11, 21], [42, 8, 9]])

print('x:\n:', x)

# reshape: transformar a matriz em um vetor coluna
print('transformação de um vetor coluna:\n', x.reshape(1, 9))

# transposição da matriz
print('x transposta\n:', x.T)

# np.sum: soma em um dado eixo, axis = {0: linha, 1:coluna}
print('soma de todos os elementos de x:', np.sum(x))
print('soma de x ao longo das linhas:', np.sum(x, axis=0))
print('soma de x ao longo das colunas:', np.sum(x, axis=1))

# np.mean: média em um dado eixo / np.median: mediana de um eixo
print('média de todos os elementos de x:', np.mean(x))
print('média de x ao longo das linhas:', np.mean(x, axis=0))
print('média de x ao longo das colunas:', np.mean(x, axis=1))

# np.where: indentificação dos índices onde uma dada condição é atendida.
cond = x % 2 == 0 # números pares
i, j = np.where(cond)
print('índice i (linhas):', i)
print('índice J (colunas):', j)






# Regressão linear

X = [-1, -0.1254125, -0.33333, -0.111111, 0.111111111, 0.333333, 0.5555556, 0.777777, 1]
Y = [-1.125125, -0.251251251, -0.53531363136, 0.365236247534, 0.63456734, 1.3262347, 1.64734734, 2.135135135, 2.32656236]

#plot dos dados
"""plt.figure(figsize=(10, 5)) #tamanho da figura
plt.plot(X, Y, 'o', label='dados originais') #está fazendo o plot
plt.legend()  #É apenas para conseguir expor a lebel acima
plt.xlabel('X')
plt.ylabel('Y')
plt.grid() #Definir o grid do plot
plt.show()"""

# transformar para numpy e vetor coluna
X, Y = np.array(X).reshape(-1, 1), np.array(Y).reshape(-1, 1)

# adicionando bias: para estimar o termo b
X2 = np.hstack((X, np.ones(X.shape)))

# estimado a e b
beta = np.linalg.pinv(X).dot(Y)
print('a estimado', beta[0][0])
print('b estimado', beta[0][0])

#plot dos dados
plt.figure(figsize=(10, 5)) #tamanho da figura
plt.plot(X, Y, 'o', label='dados originais') #está fazendo o plot
plt.plot(X, X.dot(beta), label='regressão linear')
plt.legend()  #É apenas para conseguir expor a lebel acima
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão linear com numpy')
plt.grid() #Definir o grid do plot
plt.show()




