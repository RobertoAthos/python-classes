# Estruturas condicionais

# Estrutura if
x = 1
if x > 10:
    print('X é maior que 10')


# Estrutura condicional if - else
idade = 18

if idade >= 18:
    print('Pode tirar CNH')
else:
    print('Não pode tirar CNH')

# Estrutura condicional if - elif - else
idade = 63

if idade < 12:
        faixa_etaria = 'Criança'
elif idade <  18:
     faixa_etaria = 'Adolescente'
elif idade < 60:
     faixa_etaria = 'Adulto'
else:
     faixa_etaria = 'Idoso'
print('Faixa etária:' +  faixa_etaria)

# Estruturas de repetição

# estrutura de repetição While
n = 0
while n <= 15 and n == 0:
    print('aoba')
    n = n + 1
print('Fim do bloco')

a = 15
soma = 0
contador = 0

while contador <= a:
     print('soma', soma)
     print('contador', contador)
     soma = soma + contador
     contador = contador + 1
     print('soma depois', soma)
     print('contador depois', contador)
print(f'A soma dos primeiros {n} inteiros é {soma}')

# estrutura de repetição for - in
numero = '4589'
soma = 0

for i in numero:
     #print(i)
     soma = soma + int(i)
print(f'O resultado é: {soma}')

# Vamos contar quantas letras 'a' existe na palavra Araraquara
frase = 'araraquara'
contador = 0

for i in frase:
     if i == 'a':
        contador = contador + 1
print(f'Tem {contador} letras "a" na palavra {frase}')

# Função range
## Essa função cria uma sequência numérica para a gente
#  range(inicio, fim, incremento)

n = 15
soma = 0

for i in range(n + 1):
    soma = soma + i
print(f'A soma dos inteiros {n} é igual à {soma}')