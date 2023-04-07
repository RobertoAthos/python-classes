import numpy as np

# criação de um array 1D: [1,2,3] (1 dimensão)
l = [1,2,3]
x = np.array(l)
print(f'x:{x} e shape:{x.shape}')

# criação de um array 2D: listas aninhadas
l2= [[1,2], [3,4]] # 2 elementos nas linhas e 2 elementos nas colunas
x2 = np.array(l2, dtype=float) # com dtype podemos forçar o tipo de dado do nosso array
print(f'x2:\n{x2} e shape:{x2.shape}')

# criando array contendo apenas 0´s
dim = (2,2) # nesta tupla, colocamos a dimensão(nesse caso é 2D)
x3 = np.zeros(dim) # função zeros cria o array com apenas 0
print(f'x:\n{x3} e shape:{x3.shape}')

# criando array contendo apenas 1´s
dim2 = (3,3)
x4 = np.ones(dim2) # função ones cria o array apenas com 1
print(f'x:\n{x4} e shape:{x4.shape}')

# criação de valores dentro de um intervalo
x_min, x_max = 5,15
x5 = np.linspace(start=x_min, stop=x_max, num=6)
print(f'x:{x5} e shape:{x5.shape}')

# criação da matriz identidade 
n = 6
x6 = np.eye(n)
print(f'x:\n{x6} e shape:{x6.shape}')

# criando valores aleatórios
x7 = np.random.random(size=(2,3))
print(f'x:\n{x7} e shape:{x7.shape}')