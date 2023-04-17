import my_numpy as np

#  Comparações e Indexação booleana

x = np.array([[1,2], [3,4]])
y= np.array([1.5, 3.5])
print('x:\n', x)
print('x:\n', y)

# comparação ponto a ponto
print('Comparação de um array com um escalar (>):\n', x > 2)
print('Comparação de um array com um escalar (>=):\n', x >= 2)
print('Comparação de um array com um escalar (<):\n', x < 2)
print('Comparação de um array com um escalar (<=):\n', x <= 2)
print('Comparação entre arrays (==):\n', x == y)
print('Comparação entre arrays (>):\n', x > x)
print('Comparação entre arrays (>):\n', x > y) # broadcasting

# indexação booleana
x = np.array([[1,2,7],
              [4,11,21],
              [42,8,9]])
print('x:\n', x)

# indexação booleana: retornar o número de elementos maiores que k
k = 10
cond = x > k
print(f'Condição:\n', cond)
print(f'Elementos maiores que {k}: {x[cond]}')
print(f'Número de elementos maiores que {k}: {len(x[cond])}')


