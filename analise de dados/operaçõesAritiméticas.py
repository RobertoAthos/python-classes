import numpy as np

# Funções aritiméticas: soma, subtração e divisão

x = np.ones((2,2))
y = np.eye(2)
print('x:\n', x)
print('y:\n', y)

# soma
print(f'Soma de 2 arrays:\n {x + y}')
print(f'Soma com float ou int:\n {x + 2}') #broadcasting

# substração
print(f'Subtração de 2 arrays:\n {x - y}')
print(f'Subtração com float ou int:\n {x - 2}') #broadcasting

# divisão
print(f'Divisão de 2 arrays:\n {x / y}') # Quando retornar inf, é pq não é possível dividir por 0
print(f'Divisão com float ou int:\n {x / 2}') #broadcasting

# multiplicação
print(f'Multiplicação de 2 arrays:\n {x * y}') # Quando retornar inf, é pq não é possível dividir por 0
print(f'Multiplicação com float ou int:\n {x * 2}') #broadcasting


# Operações matriciais

# multiplicação matricial
print(f'Multiplicação matricial (np.dot)d:\n', np.dot(x,y))
print(f'Multiplicação matricial python puro:\n', x @ y)
print(f'Multiplicação matricial (.dot)d:\n', x.dot(y))

