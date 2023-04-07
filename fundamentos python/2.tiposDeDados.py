# Tipos primitivos de dados e operadores


# Exemplos do tipo int, que representa números inteiros
x =3
y = -3
big = 11111112555555555555555555333333333333
print(big - y)

# Função Type, serve para verificar o tipo de uma variável ou função
print(type(x))
print(type(y))

# Exemplos tipo float, que representa números decimais
a= 3.5
b = -5.3
c = -a
pi = 3.1423462462462421465384568

print(type(a))

# Tipo bool, que é booleana
habilitado = True
pendencias = False

print(habilitado)
print(pendencias)

#Tipo str (string)
cidade = 'Porto Seguro'
nome = 'Roberto'
text = 'eu estou escrevendo um "texto"'

print(cidade)
print(nome)
print(text)

print(type(cidade))
print(type(nome))

# Tipo NoneType, que é usado para um valor null

j = None ## None == null

print(type(j))


# Operadores em Python
    # Aritiméticos = + , - , * , / , % , // , ** 
    # Comparação = > , >= , < , <= , == , !=
    # Lógicos = and(implementação), or(disjunção) , not(complemento)


# Operadores aritiméticos
x = 2 + 2 
print(x)

#Operadores de comparação
print(10>5)

#Operadores lógicos
""" idade = 23 
possui_cnh = False
print( idade > 18 and possui_cnh) # and == && """

idade = 35
possui_autorizacao = False
print (idade > 18 or possui_autorizacao)


# Operações com String
palavra = 'consolação'
print(palavra[0])
print(palavra[3:6]) ## acessa mais de um caractere

# Operações de filiação(Pertencimento)
s1 = 'consolação'
s2 = 'sola'

print(s1 in s2) ##  'in' verifica se o s1 está dentro de s2
print(s2 in s1) ## verifica se s2 está dentro de s1
print('solar' in s1)
print('solar' not in s2)

x = 'brasilia'
print('brasil' in x)

# Função e Métodos das Strings
palavra = 'Roberto'
print(len(palavra)) # 'len' vem de lenght, é usado para ver o tamanho da string

print(s1.upper()) # colocar todas as letras em maiusculo UpperCase
print(s1.lower()) # colocar todas as letras em minusculo
print(s1.title()) # coloca apenas a primeira letra em maiusculo

print(palavra.replace('Roberto', 'Bingo')) # replace é para substituição, o primeiro argumento é o que você quer substituir e o segundo é o que vai substituir
print(palavra.find('erto')) # retorna o indice da primeira ocorrência da palavra
print(palavra.startswith('Ro'))
print(palavra.endswith('rto'))

palavra2 = 'eu sou legal, e tipo assim, sou mesmo'

print(palavra2.split()) # particiona a string em outras, que são separadas por um espaço
print(palavra2.split(',')) # particiona a string em outras, que são separadas por ','


#Conversão e Formatação do tipo de dados

#Converter número em string
nascimento = 2005
ano_atual = 2023
idade = ano_atual - nascimento
hojeEmDia = 'Eu tenho ' + str(idade) + ' anos' # 'str' converte números em string
print(hojeEmDia)

#Conversão
print(float(10)) # converte número inteiro em decimal
print(bool(-1)) # sempre será True quando tiver um número
print(bool(0)) # apenas será falso caso o número for 0
print(str(999)) # converte em string

# Formatação utilizando f-strings
variavel = 15
expressao = 10 == 15
# É que nem o `` do js para deixar uma string dinâmica
f_string = f'Exemplo de f-string com um valor {variavel} e uma expressão {expressao}'
print(f_string)