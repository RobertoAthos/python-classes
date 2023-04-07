# Estruturas de Dados

# Listas (é um array)
lista = [1,2,3,4]
print(lista)

idades = [24,51,25,12,62,71,12,52,53,47,13,43,62]
maior_idade = idades[0]

for i in idades:
    if i > maior_idade:
        maior_idade = i
print('A maior idade é', maior_idade)

lista.append(5) # append() é o método para adicionar um novo item à lista
print(lista)

# Funções, Operadores e Métodos
l1 = [30,12,20]

# funções úteis
print(len(l1)) # len: retorna a quantidade de eletementos da lista (lenght)
print(sum(l1)) # sum: retorna a soma dos elementos de uma lista.
print(max(l1)) # max: retorna o maior elemento da lista

# Métodos que alteram os valores internos da lista
l1.reverse() # reverse: inverte  ordem dos elementos
print(l1)
l1.extend([40,50]) # extend: adiciona elementos de outra sequência
print(l1)
l1.sort() # sort: ordena os valores da lista
print(l1)
l1.insert(2, 'novo valor') # insert: adiciona um elemento em um índice específico
print(l1)
l1.pop() # pop: remove o último elemento da lista
print(l1)
l1.clear() # clear: limpa a lista, removendo todos os elementos
print(l1)

# Tuplas (tuple)
# Diferente das listas, a tupla não é mutável, ou seja, não tem como alterar os valores nela
tuple = (0,1,2,3,4)
print (tuple)


# Conjunto (set) (É  igual os objetos do js)

# criação de um conjunto homogêneo
c1 = {2,0,1,4,3} 
print(c1) #  a ordem não importa, ele sempre ordenará em ordem crescente

# conjunto heterogêneo
#  não ordena

# Opereções com conjuto
A = {1,2,3,4,5}
B = {6,7,8,9,10}

# Operação de União
print(A | B)
# ou
print(A.union(B))

# Operação de Diferença
print(A - B)
# ou
print(A.difference(B))

# Dicionário (dict)
# cada item é composto por uma chave e um valor
d1 = {'nome':'Roberto', 'idade': 18, 'sexo':'masculino'}
print(d1)
print(f'meu nome é {d1["nome"]} e tenho {d1["idade"]} anos')

d1['endereço'] = 'Rua Raoni'
print(d1)


# Itera sobre as chaves
d2 = {'zero': 0, 'um':1, 'dois':2, 'tres':3, 'quatro':4, 'dez':10}

for key in d2:
    if key == 'dois':
        print('Chave dois encontrada')
        break

for key in d2.keys():
    if key == 'dez':
        print('Chave 10 encontrada')
        break

# aqui vai imprimir só as chaves
for key in d2:
    print(d2[key])

# itera sobre os valores
soma = 0
for value in d2.values():
    soma = soma + value
    print('Soma dos valores:', soma)

# itera sobre os itens
for key,value in d2.items():
    print(key,value)

print(list(d2.items()))
