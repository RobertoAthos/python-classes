# Declaração de Funções

#def nome_da_funcao(argumento1,argumento2,...):
    # <bloco de codiggo>
    #return resultado

l1 = [1,2,3,4,5,6]
l2 = [12,43,51,63,12]
l3 = [12,523,613,61,63]

def soma_list(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma

def multiply_list(lista):
    mult = 1
    for i in lista:
        mult = mult * i
    return mult

soma_11 = multiply_list(l1)
soma_12 = soma_list(l2)
soma_13 = soma_list(l3)

print(f'O resultado: 11={soma_11}, 12={soma_12}, 13={soma_13}')
